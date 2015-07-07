#!/usr/bin/env python3

from PyQt5 import QtWidgets
from PyQt5 import QtCore

# TODO: support i18n

# Customize styles of QMenu
MENU_STYLE = '''
QMenu {
    background-color: #151515;
    padding: 0px;
}

QMenu::item {
    background-color: #151515;
    color: #b4b4b4;
}

QMenu::item:hover {
    background-color: #252525;
}

QMenu::item:selected {
    background-color: #353535;
}

QMenu::separator {
    background-color: #717171;
    height: 1px;
    margin-left: 5px;
    margin-right: 5px;
}
'''

class PreferencesMenu(QtWidgets.QMenu):
    '''Repalce Menu class in QML.

    A serious bug exists in QML 2.2 and Deepin 2014.3, which results in
    blank screen when a qml menu popups.
    '''

    balancedChecked = QtCore.pyqtSignal()
    speedChecked = QtCore.pyqtSignal()
    qualityChecked = QtCore.pyqtSignal()
    fullscreenToggled = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        group = QtWidgets.QActionGroup(self)

        balancedAction = QtWidgets.QAction('Balance', self)
        balancedAction.setCheckable(True)
        balancedAction.setChecked(True)
        balancedAction.triggered.connect(self.balancedChecked)
        balancedAction.setActionGroup(group)

        speedAction = QtWidgets.QAction('Optimize Speed', self)
        speedAction.setCheckable(True)
        speedAction.triggered.connect(self.speedChecked)
        speedAction.setActionGroup(group)

        qualityAction = QtWidgets.QAction('Optimize Quality', self)
        qualityAction.setCheckable(True)
        qualityAction.triggered.connect(self.qualityChecked)
        qualityAction.setActionGroup(group)

        fullscreenAction = QtWidgets.QAction('Fullscreen', self)
        fullscreenAction.toggled.connect(self.fullscreenToggled)
        fullscreenAction.setCheckable(True)

        self.addAction(balancedAction)
        self.addAction(speedAction)
        self.addAction(qualityAction)
        self.addSeparator()
        self.addAction(fullscreenAction)

        self.setStyleSheet(MENU_STYLE)
