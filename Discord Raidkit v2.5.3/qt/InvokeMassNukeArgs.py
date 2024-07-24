# Form implementation generated from reading ui file 'InvokeMassNukeArgs.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgInvokeMassNukeArgs(object):
    def setupUi(self, dlgInvokeMassNukeArgs):
        dlgInvokeMassNukeArgs.setObjectName("dlgInvokeMassNukeArgs")
        dlgInvokeMassNukeArgs.resize(320, 380)
        dlgInvokeMassNukeArgs.setMinimumSize(QtCore.QSize(320, 380))
        dlgInvokeMassNukeArgs.setMaximumSize(QtCore.QSize(320, 380))
        self.btnBox = QtWidgets.QDialogButtonBox(parent=dlgInvokeMassNukeArgs)
        self.btnBox.setGeometry(QtCore.QRect(10, 330, 301, 32))
        self.btnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btnBox.setObjectName("btnBox")
        self.leMemberID = QtWidgets.QLineEdit(parent=dlgInvokeMassNukeArgs)
        self.leMemberID.setGeometry(QtCore.QRect(20, 90, 280, 20))
        self.leMemberID.setObjectName("leMemberID")
        self.lblMemberID = QtWidgets.QLabel(parent=dlgInvokeMassNukeArgs)
        self.lblMemberID.setGeometry(QtCore.QRect(20, 30, 281, 16))
        self.lblMemberID.setObjectName("lblMemberID")
        self.lblMemberID2 = QtWidgets.QLabel(parent=dlgInvokeMassNukeArgs)
        self.lblMemberID2.setGeometry(QtCore.QRect(20, 45, 281, 16))
        self.lblMemberID2.setObjectName("lblMemberID2")
        self.lblNotRequired = QtWidgets.QLabel(parent=dlgInvokeMassNukeArgs)
        self.lblNotRequired.setGeometry(QtCore.QRect(20, 70, 271, 21))
        self.lblNotRequired.setObjectName("lblNotRequired")
        self.lblGuildTitle = QtWidgets.QLabel(parent=dlgInvokeMassNukeArgs)
        self.lblGuildTitle.setGeometry(QtCore.QRect(20, 140, 281, 21))
        self.lblGuildTitle.setObjectName("lblGuildTitle")
        self.leGuildTitle = QtWidgets.QLineEdit(parent=dlgInvokeMassNukeArgs)
        self.leGuildTitle.setGeometry(QtCore.QRect(20, 180, 280, 20))
        self.leGuildTitle.setObjectName("leGuildTitle")
        self.lblNotRequired_2 = QtWidgets.QLabel(parent=dlgInvokeMassNukeArgs)
        self.lblNotRequired_2.setGeometry(QtCore.QRect(20, 160, 271, 21))
        self.lblNotRequired_2.setObjectName("lblNotRequired_2")
        self.lblAvatarPath = QtWidgets.QLabel(parent=dlgInvokeMassNukeArgs)
        self.lblAvatarPath.setGeometry(QtCore.QRect(20, 230, 281, 21))
        self.lblAvatarPath.setObjectName("lblAvatarPath")
        self.leAvatarPath = QtWidgets.QLineEdit(parent=dlgInvokeMassNukeArgs)
        self.leAvatarPath.setGeometry(QtCore.QRect(20, 270, 251, 20))
        self.leAvatarPath.setObjectName("leAvatarPath")
        self.lblNotRequired_3 = QtWidgets.QLabel(parent=dlgInvokeMassNukeArgs)
        self.lblNotRequired_3.setGeometry(QtCore.QRect(20, 250, 271, 21))
        self.lblNotRequired_3.setObjectName("lblNotRequired_3")
        self.btnGetAvatar = QtWidgets.QPushButton(parent=dlgInvokeMassNukeArgs)
        self.btnGetAvatar.setGeometry(QtCore.QRect(280, 270, 21, 21))
        self.btnGetAvatar.setObjectName("btnGetAvatar")

        self.retranslateUi(dlgInvokeMassNukeArgs)
        self.btnBox.accepted.connect(dlgInvokeMassNukeArgs.accept) # type: ignore
        self.btnBox.rejected.connect(dlgInvokeMassNukeArgs.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgInvokeMassNukeArgs)

        self.btnGetAvatar.clicked.connect(self.getAvatar)

    def retranslateUi(self, dlgInvokeMassNukeArgs):
        _translate = QtCore.QCoreApplication.translate
        dlgInvokeMassNukeArgs.setWindowTitle(_translate("dlgInvokeMassNukeArgs", "Mass Nuke Arguments"))
        self.lblMemberID.setText(_translate("dlgInvokeMassNukeArgs", "Enter the member id of the member"))
        self.lblMemberID2.setText(_translate("dlgInvokeMassNukeArgs", "to exclude from the nuke"))
        self.lblNotRequired.setText(_translate("dlgInvokeMassNukeArgs", "(This field is not required)"))
        self.lblGuildTitle.setText(_translate("dlgInvokeMassNukeArgs", "Enter a name to rename the server to"))
        self.lblNotRequired_2.setText(_translate("dlgInvokeMassNukeArgs", "(This field is not required)"))
        self.lblAvatarPath.setText(_translate("dlgInvokeMassNukeArgs", "Enter a full file path to a new server avatar"))
        self.lblNotRequired_3.setText(_translate("dlgInvokeMassNukeArgs", "(This field is not required)"))
        self.btnGetAvatar.setText(_translate("dlgInvokeMassNukeArgs", "..."))

    def getAvatar(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image", "", "Image Files (*.png *.jpg *.bmp)"
        )
        self.leAvatarPath.setText(filename[0])
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgInvokeMassNukeArgs = QtWidgets.QDialog()
    ui = Ui_dlgInvokeMassNukeArgs()
    ui.setupUi(dlgInvokeMassNukeArgs)
    dlgInvokeMassNukeArgs.show()
    sys.exit(app.exec())