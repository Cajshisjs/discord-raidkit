# Form implementation generated from reading ui file 'InvokeNukeArgs.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgInvokeNukeArgs(object):
    def setupUi(self, dlgInvokeNukeArgs):
        dlgInvokeNukeArgs.setObjectName("dlgInvokeNukeArgs")
        dlgInvokeNukeArgs.resize(320, 380)
        dlgInvokeNukeArgs.setMinimumSize(QtCore.QSize(320, 380))
        dlgInvokeNukeArgs.setMaximumSize(QtCore.QSize(320, 380))
        self.btnBox = QtWidgets.QDialogButtonBox(parent=dlgInvokeNukeArgs)
        self.btnBox.setGeometry(QtCore.QRect(10, 330, 301, 32))
        self.btnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btnBox.setObjectName("btnBox")
        self.leMemberID = QtWidgets.QLineEdit(parent=dlgInvokeNukeArgs)
        self.leMemberID.setGeometry(QtCore.QRect(20, 90, 280, 20))
        self.leMemberID.setObjectName("leMemberID")
        self.lblMemberID = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblMemberID.setGeometry(QtCore.QRect(20, 30, 281, 16))
        self.lblMemberID.setObjectName("lblMemberID")
        self.lblMemberID2 = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblMemberID2.setGeometry(QtCore.QRect(20, 45, 281, 16))
        self.lblMemberID2.setObjectName("lblMemberID2")
        self.lblNotRequired = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblNotRequired.setGeometry(QtCore.QRect(20, 70, 271, 21))
        self.lblNotRequired.setObjectName("lblNotRequired")
        self.lblGuildTitle = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblGuildTitle.setGeometry(QtCore.QRect(20, 140, 281, 21))
        self.lblGuildTitle.setObjectName("lblGuildTitle")
        self.leGuildTitle = QtWidgets.QLineEdit(parent=dlgInvokeNukeArgs)
        self.leGuildTitle.setGeometry(QtCore.QRect(20, 180, 280, 20))
        self.leGuildTitle.setObjectName("leGuildTitle")
        self.lblNotRequired_2 = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblNotRequired_2.setGeometry(QtCore.QRect(20, 160, 271, 21))
        self.lblNotRequired_2.setObjectName("lblNotRequired_2")
        self.lblAvatarPath = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblAvatarPath.setGeometry(QtCore.QRect(20, 230, 281, 21))
        self.lblAvatarPath.setObjectName("lblAvatarPath")
        self.leAvatarPath = QtWidgets.QLineEdit(parent=dlgInvokeNukeArgs)
        self.leAvatarPath.setGeometry(QtCore.QRect(20, 270, 251, 20))
        self.leAvatarPath.setObjectName("leAvatarPath")
        self.lblNotRequired_3 = QtWidgets.QLabel(parent=dlgInvokeNukeArgs)
        self.lblNotRequired_3.setGeometry(QtCore.QRect(20, 250, 271, 21))
        self.lblNotRequired_3.setObjectName("lblNotRequired_3")
        self.btnGetAvatar = QtWidgets.QPushButton(parent=dlgInvokeNukeArgs)
        self.btnGetAvatar.setGeometry(QtCore.QRect(280, 270, 21, 21))
        self.btnGetAvatar.setObjectName("btnGetAvatar")

        self.retranslateUi(dlgInvokeNukeArgs)
        self.btnBox.accepted.connect(dlgInvokeNukeArgs.accept) # type: ignore
        self.btnBox.rejected.connect(dlgInvokeNukeArgs.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgInvokeNukeArgs)

        self.btnGetAvatar.clicked.connect(self.getAvatar)

    def retranslateUi(self, dlgInvokeNukeArgs):
        _translate = QtCore.QCoreApplication.translate
        dlgInvokeNukeArgs.setWindowTitle(_translate("dlgInvokeNukeArgs", "Nuke Arguments"))
        self.lblMemberID.setText(_translate("dlgInvokeNukeArgs", "Enter the member id of the member"))
        self.lblMemberID2.setText(_translate("dlgInvokeNukeArgs", "to exclude from the nuke"))
        self.lblNotRequired.setText(_translate("dlgInvokeNukeArgs", "(This field is not required)"))
        self.lblGuildTitle.setText(_translate("dlgInvokeNukeArgs", "Enter a name to rename the server to"))
        self.lblNotRequired_2.setText(_translate("dlgInvokeNukeArgs", "(This field is not required)"))
        self.lblAvatarPath.setText(_translate("dlgInvokeNukeArgs", "Enter a full file path to a new server avatar"))
        self.lblNotRequired_3.setText(_translate("dlgInvokeNukeArgs", "(This field is not required)"))
        self.btnGetAvatar.setText(_translate("dlgInvokeNukeArgs", "..."))
    
    def getAvatar(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.bmp)"
        )
        self.leAvatarPath.setText(filename[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgInvokeNukeArgs = QtWidgets.QDialog()
    ui = Ui_dlgInvokeNukeArgs()
    ui.setupUi(dlgInvokeNukeArgs)
    dlgInvokeNukeArgs.show()
    sys.exit(app.exec())