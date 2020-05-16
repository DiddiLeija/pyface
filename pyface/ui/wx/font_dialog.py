# (C) Copyright 2005-2020 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

""" The interface for a dialog that allows the user to select a font. """

import wx

from traits.api import provides

from pyface.font import Font, PyfaceFont
from pyface.i_font_dialog import IFontDialog
from .dialog import Dialog


@provides(IFontDialog)
class FontDialog(Dialog):
    """ A dialog for selecting fonts.
    """

    #: A Font instance that holds the initial font at the start and tracks
    #: the selected font during user interactions.
    font = PyfaceFont()

    # ------------------------------------------------------------------------
    # 'IDialog' interface.
    # ------------------------------------------------------------------------

    def _create_contents(self, parent):
        # In wx this is a canned dialog.
        pass

    # ------------------------------------------------------------------------
    # 'IWindow' interface.
    # ------------------------------------------------------------------------

    def close(self):
        font_data = self.control.GetFontData()
        wx_font = font_data.GetChosenFont()
        self.font = Font.from_toolkit(wx_font)
        super(FontDialog, self).close()

    # ------------------------------------------------------------------------
    # 'IWidget' interface.
    # ------------------------------------------------------------------------

    def _create_control(self, parent):
        wx_font = self.font.to_toolkit()
        data = wx.FontData()
        data.SetInitialFont(wx_font)
        dialog = wx.FontDialog(parent, data)
        return dialog