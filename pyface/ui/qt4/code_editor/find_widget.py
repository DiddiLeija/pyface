#------------------------------------------------------------------------------
# Copyright (c) 2010, Enthought Inc
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license.

#
# Author: Enthought Inc
# Description: <Enthought pyface code editor>
#------------------------------------------------------------------------------

import weakref

from qtpy import QtCore, QtWidgets


class FindWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(FindWidget, self).__init__(parent)
        self.adv_code_widget = weakref.ref(parent)

        self.button_size = self.fontMetrics().width('Replace All') + 20

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow('Fin&d', self._create_find_control())

        layout = QtWidgets.QHBoxLayout()
        layout.addLayout(form_layout)

        close_button = QtWidgets.QPushButton('Close')
        layout.addWidget(close_button, 1, QtCore.Qt.AlignRight)
        close_button.clicked.connect(self.hide)

        self.setLayout(layout)

    def setFocus(self):
        self.line_edit.setFocus()

    def _create_find_control(self):
        control = QtWidgets.QWidget(self)

        self.line_edit = QtWidgets.QLineEdit()
        self.next_button = QtWidgets.QPushButton('&Next')
        self.next_button.setFixedWidth(self.button_size)
        self.prev_button = QtWidgets.QPushButton('&Prev')
        self.prev_button.setFixedWidth(self.button_size)
        self.options_button = QtWidgets.QPushButton('&Options')
        self.options_button.setFixedWidth(self.button_size)

        options_menu = QtWidgets.QMenu(self)
        self.case_action = QtWidgets.QAction('Match &case', options_menu)
        self.case_action.setCheckable(True)
        self.word_action = QtWidgets.QAction('Match words', options_menu)
        self.word_action.setCheckable(True)
        self.wrap_action = QtWidgets.QAction('Wrap search', options_menu)
        self.wrap_action.setCheckable(True)
        self.wrap_action.setChecked(True)
        options_menu.addAction(self.case_action)
        options_menu.addAction(self.word_action)
        options_menu.addAction(self.wrap_action)
        self.options_button.setMenu(options_menu)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.next_button)
        layout.addWidget(self.prev_button)
        layout.addWidget(self.options_button)
        layout.addStretch(2)
        layout.setContentsMargins(0, 0, 0, 0)

        control.setLayout(layout)
        return control

