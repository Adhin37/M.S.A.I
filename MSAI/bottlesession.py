#!/usr/bin/env python
#
#  Bottle session manager.  See README for full documentation.
#
#  Written by: Sean Reifschneider <jafo@tummy.com>
#
#  License: 3-clause BSD

from __future__ import with_statement

import pickle
import os
import uuid
import time
import bottle


def authenticator(session_manager, login_url='/auth/login'):
    '''Create an authenticator decorator.

    :param session_manager: A session manager class to be used for storing
            and retrieving session data.  Probably based on
            :class:`BaseSession`.
    :param login_url: The URL to redirect to if a login is required.
            (default: ``'/auth/login'``).
    '''
    def valid_user(login_url=login_url):
        """Save session."""
        def decorator(handler):
            """No idea."""
            import functools

            @functools.wraps(handler)
            def check_auth(*a, **ka):
                """Check authentificate."""
                try:
                    data = session_manager.get_session()
                    if not data['valid']:
                        raise KeyError('Invalid login')
                except (KeyError, TypeError):
                    bottle.response.set_cookie(
                        'validuserloginredirect',
                        bottle.request.fullpath, path='/',
                        expires=(int(time.time()) + 3600))
                    bottle.redirect(login_url)

                #  set environment
                if data.get('name'):
                    bottle.request.environ['REMOTE_USER'] = data['name']

                return handler(*a, **ka)
            return check_auth
        return decorator
    return valid_user

class BaseSession(object):
    '''Base class which implements some of the basic functionality required for
    session managers.  Cannot be used directly.

    :param cookie_expires: Expiration time of session ID cookie, either `None`
            if the cookie is not to expire, a number of seconds in the future,
            or a datetime object.  (default: 30 days)
    '''
    def __init__(self, cookie_expires=86400 * 30):
        self.cookie_expires = cookie_expires

    def load(self, sessionid):
        """Load session."""
        raise NotImplementedError

    def save(self, sessionid, data):
        """Save session."""
        raise NotImplementedError

    def make_session_id(self):
        """Create session id."""
        return str(uuid.uuid4())

    def allocate_new_session_id(self):
        """Retry allocating a unique sessionid."""
        allocaterange = 1
        while allocaterange < 100:
            sessionid = self.make_session_id()
            if not self.load(sessionid):
                return sessionid
        allocaterange += 1
        raise ValueError('Unable to allocate unique session')

    def get_session(self):
        """Get existing or create new session identifier."""
        sessionid = bottle.request.get_cookie('sessionid')
        if not sessionid:
            sessionid = self.allocate_new_session_id()
            bottle.response.set_cookie(
                'sessionid', sessionid, path='/',
                expires=(int(time.time()) + self.cookie_expires))

        #  load existing or create new session
        data = self.load(sessionid)
        if not data:
            data = {'sessionid': sessionid, 'valid': False}
            self.save(data)

        return data


class PickleSession(BaseSession):
    '''Class which stores session information in the file-system.

    :param session_dir: Directory that session information is stored in.
            (default: ``'/tmp'``).
    '''
    def __init__(self, session_dir='/tmp', *args, **kwargs):
        super(PickleSession, self).__init__(*args, **kwargs)
        self.session_dir = session_dir

    def load(self, sessionid):
        filename = os.path.join(self.session_dir, 'session-%s' % sessionid)
        if not os.path.exists(filename):
            return None
        with open(filename, 'r') as filepath:
            session = pickle.load(filepath)
        return session

    def save(self, data):
        """Save session."""
        sessionid = data['sessionid']
        sessionfilename = os.path.join(self.session_dir, 'session-%s' % sessionid)
        sessiontmpname = sessionfilename + '.' + str(uuid.uuid4())
        with open(sessiontmpname, 'w') as filepath:
            self.session = pickle.dump(data,filepath)
        os.rename(sessiontmpname, sessionfilename)


class CookieSession(BaseSession):
    '''Session manager class which stores session in a signed browser cookie.

    :param cookie_name: Name of the cookie to store the session in.
            (default: ``session_data``)
    :param secret: Secret to be used for "secure cookie".  If ``None``,
            a random secret will be generated and written to a temporary
            file for future use.  This may not be suitable for systems which
            have untrusted users on it.  (default: ``None``)
    :param secret_file: File to read the secret from.  If ``secret`` is
            ``None`` and ``secret_file`` is set, the first line of this file
            is read, and stripped, to produce the secret.
    '''

    def __init__(
            self, secret=None, secret_file=None, cookie_name='session_data',
            secure=False, httponly=True, *args, **kwargs):

        super(CookieSession, self).__init__(*args, **kwargs)
        self.cookie_name = cookie_name
        self.secure = secure
        self.httponly = httponly

        if not secret and secret_file is not None:
            with open(secret_file, 'r') as filepath:
                secret = filepath.readline().strip()

        if not secret:
            import string
            import random
            import tempfile
            import sys

            tmpfilename = os.path.join(
                tempfile.gettempdir(),
                '%s.secret' % os.path.basename(sys.argv[0]))

            if os.path.exists(tmpfilename):
                with open(tmpfilename, 'r') as filepath:
                    secret = filepath.readline().strip()
            else:
                #  save off a secret to a tmp file
                secret = ''.join([
                    random.choice(string.letters)
                    for x in range(32)])

                old_umask = os.umask(int('077', 8))
                with open(tmpfilename, 'w') as filepath:
                    filepath.write(secret)
                os.umask(old_umask)

        self.secret = secret

    def load(self, sessionid):
        cookie = bottle.request.get_cookie(
            self.cookie_name,
            secret=self.secret)
        if cookie is None:
            return {}
        return pickle.loads(cookie)

    def save(self, data):
        """Save."""
        args = dict(secret=self.secret,
                    path='/', expires=int(time.time()) + self.cookie_expires)
        if self.secure:
            args['secure'] = True
        if self.httponly:
            args['httponly'] = True

        bottle.response.set_cookie(
            self.cookie_name, pickle.dumps(data), **args)
