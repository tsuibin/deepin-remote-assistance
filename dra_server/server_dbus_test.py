#!/usr/bin/env python3

import sys
sys.path.insert(0, '..')

from PyQt5 import QtCore

from dra_server.server_dbus import is_server_dbus_running
from dra_server.server_dbus import ServerDBus
from dra_utils.log import server_log

def main():
    if is_server_dbus_running():
        print('server dbus is running, ignore')
        return
    server_dbus = ServerDBus()
    # FIXME: log service failed to dump log
    server_log.debug('Init server dbus: %s' % server_dbus)
    print('server dbus inited')
    app = QtCore.QCoreApplication(sys.argv)
    app.exec()

if __name__ == '__main__':
    main()
