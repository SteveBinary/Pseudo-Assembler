from PyQt5.QtGui import QFont, QRegExpValidator, QTextCursor, QColor
from PyQt5.QtCore import QRegExp, Qt, QTimer
from PyQt5.QtWidgets import *
from QProgramWindow import Ui_MainWindow
from QDialogSpeicherzellen import Ui_Dialog_Speicher
from QDialogInsSet import Ui_QDialog_inset
from QDialogDefaultInsSet import Ui_Dialog
from REGISTER import INPUT, OUTPUT
from CACHE import CACHE
from ALU import ALU
from CU import CU, encode_instruction
import re, sys, os

app = QApplication(sys.argv)
main_window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(main_window)

# Fenstergröße / Position: Zentriert und 2/3 der Bildschirmgröße
width = int(app.primaryScreen().size().width() / 3 * 2)
height = int(app.primaryScreen().size().height() / 3 * 2)
x_pos = int((app.primaryScreen().size().width() - width) / 2)
y_pos = int((app.primaryScreen().size().height() - height) / 2)
main_window.setGeometry(x_pos, y_pos, width, height)

# globale Variablen
global instruction_set, instruction_set_text, saved, current_file, prev_current_file, interval, timer, cycle, cu, prev_programm_counter
global offset, missing_op, code_factorial, code_digit_sum, code_sum_a_to_b_with_loop, code_sum_a_to_b_without_loop, code_mean_value_3_numbers
global code_mean_value_arbitrary, cell_number
instruction_set = []
instruction_set_text = "ld\nst\nin\nout\nadd\nsub\nmul\ndiv\nmod\ncmp\njmp\njlt\njeq\njgt\nend"
saved = True
current_file = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
prev_current_file = ""
interval = 0
timer = QTimer()
cycle = 0
cu = None
prev_programm_counter = 0
offset = 0
missing_op = False
cell_number = 64


# ======================================================================================= #
# ================================ methods ============================================== #


def get_instruction_set(source: str):
    """
    Den aktuellen Befehlssatz aus der Textdatei (source) laden.
    """
    try:
        with open(source, "r") as f:
            global instruction_set_text
            instruction_set_text = f.read()

        with open(source, "r") as f:
            global instruction_set
            instruction_set = []
            for l in f.readlines():
                instruction_set.append(l.strip())
    except:
        message_box_errors(["Fehler beim Laden des Befehlssatzes!"])


def load(source_code: str):
    """
    Kompiliert den Quellcode aus dem Code Editor, speichert die kodierten Befehle im Speicher und visualisiert gleichzeitig das Speicherwerk.
    """
    setup_ram(cell_number)  # Die Anzahl der Speicherzellen setzen
    get_instruction_set("instruction_set.txt")  # Den aktuellen Befehlssatz laden
    global cu, offset
    cu = CU(ui, instruction_set, timer, CACHE(), ALU(), INPUT(), OUTPUT()) 

    end = 0
    cell = 0
    variables = dict()
    errors = []
    offset = 0
    line_number = 0

    # Den Quellcode durchgehen, Fehler erkennen und Kompilation
    for line in source_code.splitlines(False):
        line_number += 1
        line = line.split("#")[0]  # Kommentare ausschließen
        global missing_op
        missing_op = False

        if not line.isspace() and line != "":
            c = re.sub(" +", " ", line.replace("\n","").replace("  ", " ")).strip().split(" ")

            if len(c) < 2 and c[0] in instruction_set[:14]:
                errors.append(str(line_number) + ": Fehlender Operand")
                missing_op = True

            if c[0].strip() == "def" and not missing_op:
                def_line = re.sub(" +", " ", " ".join(c).replace("def ", "").replace("=", "  ")).split(" ")
                if len(def_line) != 2 or "=" not in "".join(c):
                    errors.append(str(line_number) + ": Inkorrekte Initialisierung einer Variable " + " ".join(c))
                elif def_line[0] != "" and def_line[0][0].isalpha():
                    if def_line[-1].startswith("@") and def_line[-1].replace("@", "").replace(".", "").replace("-", "").isdigit():
                        variables[def_line[0].strip()] = "@" + str(abs(int(float(def_line[-1].replace("@", "").strip()))))
                    elif def_line[-1].replace(".", "").replace("-", "").isdigit():
                        variables[def_line[0].strip()] = str(int(float(def_line[-1].strip())))
                    else:
                        errors.append(str(line_number) + ": Inkorrekte Initialisierung einer Variable " + " ".join(c))
                else:
                    errors.append(str(line_number) + ": Das erste Zeichen eines Variablennamens muss ein Buchstabe sein!")
                cell -= 2
                offset += 1

            elif c[0].strip() not in instruction_set:
                errors.append(str(line_number) + ": unbekannter Befehl: " + c[0])

            elif instruction_set[14] == c[0]:
                cu.CACHE.write(end, c[0].strip())
                write_ui_ram(end, c[0].strip(), "0")

            elif c[0].strip() in instruction_set[10:13] and not missing_op:
                cu.CACHE.write(cell, c[0].strip())
                cu.CACHE.write(cell + 1, str(int(float(c[1].strip()) - offset)))
                write_ui_ram(cell, c[0].strip(), str(int(float(c[1].strip()) - offset)))
                end += 2

            elif not missing_op:
                cu.CACHE.write(cell, c[0].strip())
                if c[1].startswith("@"):
                    cu.CACHE.write(cell + 1, "@" + str(abs(int(float(c[1].replace("@", "").strip())))))
                    write_ui_ram(cell, c[0].strip(), "@" + str(abs(int(float(c[1].replace("@", "").strip())))))
                else:
                    try:
                        cu.CACHE.write(cell + 1, str(int(float(c[1].strip()))))
                        write_ui_ram(cell, c[0].strip(), str(int(float(c[1].strip()))))
                    except:
                        if c[1] in variables.keys():
                            if variables[c[1].strip()].startswith("@"):
                                cu.CACHE.write(cell + 1, "@" + str(abs(int(float(variables[c[1].strip()].replace("@", "").strip())))))
                                write_ui_ram(cell, c[0].strip(), "@" + str(abs(int(float(variables[c[1].strip()].replace("@", "").strip())))))
                            else:
                                cu.CACHE.write(cell + 1, str(int(float(variables[c[1].strip()]))))
                                write_ui_ram(cell, c[0].strip(), str(int(float(variables[c[1].strip()]))))
                        else:
                            errors.append(str(line_number) + ": Variable '" + c[1] + "' wurde noch nicht initialisiert!")

                end += 2

            cell += 2

        else:
            offset += 1

    if len(errors) > 0:
        message_box_errors(errors)
        return False

    ui.actionFakult_t.setEnabled(False)
    ui.actionQuersumme.setEnabled(False)
    ui.actionSumme_a_bis_b_mit_Schleife.setEnabled(False)
    ui.actionSumme_a_bis_b_ohne_Schleife.setEnabled(False)
    ui.actionDurchschnitt_dreier_Zahlen_floor.setEnabled(False)
    ui.actionBefehlssatz_ver_ndern.setEnabled(False)
    ui.actionZahl_der_angezeigten_Speicherzellen.setEnabled(False)
    ui.actionDurchschnitt_beliebig_vieler_Zahlen.setEnabled(False)
    return True


def message_box_errors(errors: list):
    """
    Fenster, das alle Elemente aus errors anzeigt
    """
    info = QMessageBox()
    info.setIcon(QMessageBox.Critical)
    info.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint)
    font = QFont()
    font.setPointSize(10)
    info.setFont(font)
    info.setText("\n".join(errors))
    info.setWindowTitle("Fehler")
    info.exec_()


def run_vn():
    """
    Führt immer die nächste VN-Phase aus (Fetch, Decode oder Execute) und setzt die Labels in der GUI.
    """
    global cycle, timer, cu
    
    if cycle >= 3:
        cycle = 0

    try:
        if cycle == 0:
            # Bei neuem Zyklus wird im Code Editor und im Speicherwerk eine neue Zeile matkiert
            cursor = QTextCursor(ui.Editor.document().findBlockByLineNumber(int(cu.program_counter / 2) + offset))
            ui.Editor.setTextCursor(cursor)
            if int(cu.program_counter / 2) < ui.Speicher.rowCount():
                global prev_programm_counter
                for j in range(ui.Speicher.columnCount()):
                    try:
                        if int(prev_programm_counter / 2) % 2 == 0:
                            ui.Speicher.item(int(prev_programm_counter / 2), j).setBackground(QColor("#DCDCDC"))
                        else:
                            ui.Speicher.item(int(prev_programm_counter / 2), j).setBackground(QColor(Qt.white))
                        ui.Speicher.item(int(cu.program_counter / 2), j).setBackground(QColor(Qt.green).lighter(150))
                    except:
                        pass
                prev_programm_counter = cu.program_counter

            ui.label_which_cycle.setText("FETCH")
            cu.fetch()
        elif cycle == 1:
            ui.label_which_cycle.setText("DECODE")
            cu.decode()
        elif cycle == 2:
            ui.label_which_cycle.setText("EXECUTE")
            cu.execute()

        ui.label_operand.setText(cu.ALU.operand)
        ui.label_operation.setText(cu.ALU.operation)
        ui.label_accu.setText(cu.ALU.acc)
        ui.label_result.setText(cu.ALU.result)

        cycle += 1
    except Exception as e:
        stop()
        if type(e) == ZeroDivisionError:
            message_box_errors([str(int(cu.program_counter / 2) + offset) + ": Division durch 0"])
        else:
            message_box_errors([str(int(cu.program_counter / 2) + offset + 1) + ": Ein Fehler ist aufgetreten!"])

    if cu.program_counter == -1:
        stop()


def start():
    """
    Wird ausgeführt, wenn "Start" gedrückt wird. Setzt die GUI zurück und startet den Timer.
    """
    if not load(ui.Editor.toPlainText()):
        return

    ui.label_which_cycle.setText("IDLE")
    ui.output_reg.setText("")
    ui.input_reg.setText("")
    ui.input_reg.setPlaceholderText("")
    ui.input_reg.setEnabled(False)
    ui.label_befehlszaehler.setText("0")
    ui.label_befehlsreg_1.setText("0")
    ui.label_befehlsreg_2.setText("0")
    ui.label_dekodierer_1.setText("0")
    ui.label_dekodierer_2.setText("0")
    ui.label_accu.setText("0")
    ui.label_operand.setText("0")
    ui.label_operation.setText(" ")
    ui.label_result.setText("0")

    if ui.actionVNPhasen.isChecked():
        ui.button_weiter.setEnabled(True)
    else:
        ui.button_weiter.setEnabled(False)

    ui.button_start.setEnabled(False)
    ui.button_stop.setEnabled(True)

    global timer, cycle, interval, cu

    timer = QTimer()
    cycle = 0

    timer.setInterval(int(interval * 1000 / 3))
    ui.Editor.setTextInteractionFlags(Qt.TextSelectableByKeyboard)
    ui.Editor.setTextCursor(QTextCursor(ui.Editor.document().findBlockByLineNumber(offset)))
    if interval >= 0:
        timer.timeout.connect(lambda: run_vn())
    timer.start()
    cu.timer = timer
    run_vn()


def stop():
    """
    Wird ausgeführt, wenn "Beenden" gedrückt wird. Setzt die GUI zurück und beendet den Timer.
    """
    timer.stop()
    ui.button_weiter.setEnabled(False)
    ui.button_start.setEnabled(True)
    ui.button_stop.setEnabled(False)
    ui.Editor.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)
    ui.input_reg.setPlaceholderText("")
    ui.input_reg.setText("")
    ui.input_reg.setEnabled(False)
    ui.Editor.setFocus()

    ui.actionFakult_t.setEnabled(True)
    ui.actionQuersumme.setEnabled(True)
    ui.actionSumme_a_bis_b_mit_Schleife.setEnabled(True)
    ui.actionSumme_a_bis_b_ohne_Schleife.setEnabled(True)
    ui.actionDurchschnitt_beliebig_vieler_Zahlen.setEnabled(True)
    ui.actionDurchschnitt_dreier_Zahlen_floor.setEnabled(True)
    ui.actionBefehlssatz_ver_ndern.setEnabled(True)
    ui.actionZahl_der_angezeigten_Speicherzellen.setEnabled(True)

    if int(cu.program_counter / 2) < ui.Speicher.rowCount():
        global prev_programm_counter
        for j in range(ui.Speicher.columnCount()):
            try:
                if int(prev_programm_counter / 2) % 2 == 0:
                    ui.Speicher.item(int(prev_programm_counter / 2),j).setBackground(QColor(QColor("#DCDCDC")))
                else:
                    ui.Speicher.item(int(prev_programm_counter / 2),j).setBackground(QColor(Qt.white))
            except:
                pass


def write_ui_ram(adr: str, instruction: str, val: str):
    """
    Trägt einen Befehl und den dazugehörigen Wert (kodiert) in das Speicherwerk (GUI) an die Adresse ein.
    """
    try:
        enc = encode_instruction(instruction_set, instruction, val)
        ui.Speicher.setItem(int(adr / 2), 1, QTableWidgetItem(enc[0]))
        ui.Speicher.setItem(int(adr / 2), 3, QTableWidgetItem(enc[1]))
    except:
        pass


def setup_ram(cell_count: int):
    """
    Setup des Speicherwerks (GUI)
    """
    ui.Speicher.setColumnCount(4)
    ui.Speicher.setRowCount(round(cell_count / 2 + 0.2))
    ui.Speicher.setHorizontalHeaderLabels(["Adr", "Wert", "Adr", "Wert"])
    font = QFont()
    font.setPointSize(15)
    font.setBold(True)
    header = ui.Speicher.horizontalHeader()
    header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(1, QHeaderView.Stretch)
    header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QHeaderView.Stretch)
    ui.Speicher.setHorizontalHeader(header)
    i = 0
    while i < ui.Speicher.rowCount():
        it1 = QTableWidgetItem(str(i * 2))
        it1.setFont(font)
        it2 = QTableWidgetItem(str(i * 2 + 1))
        it2.setFont(font)
        ui.Speicher.setItem(i, 0, it1)
        ui.Speicher.setItem(i, 1, QTableWidgetItem("0"))
        ui.Speicher.setItem(i, 2, it2)
        ui.Speicher.setItem(i, 3, QTableWidgetItem("0"))
        i += 1


def setup_demo():
    """
    Lädt die Demos mit dem aktuellen Befehlssatz neu.
    """
    global code_factorial, code_digit_sum, code_sum_a_to_b_with_loop, code_sum_a_to_b_without_loop
    global code_mean_value_3_numbers, code_mean_value_arbitrary

    code_factorial = "# Fakultät\n\ndef a = @30\ndef b = @31\n\n" + instruction_set[2] + "  a\n" + instruction_set[0] + "  1\n" + \
                     instruction_set[1] + "  b\n" + instruction_set[0] + "  a\n" + instruction_set[9] + " 2\n" + \
                     instruction_set[11] + " 18\n  " + instruction_set[6] + " b\n  " + instruction_set[1] + "  b\n  " + \
                     instruction_set[0] + "  a\n  " + instruction_set[5] + " 1\n  " + instruction_set[1] + "  a\n" + \
                     instruction_set[10] + " 9\n" + instruction_set[3] + " b\n" + instruction_set[14]
    code_digit_sum = "# Quersumme\n\ndef a = @28\ndef b = @29\n\n" + instruction_set[2] + "  a\n" + instruction_set[0] + "  a\n" + \
                     instruction_set[9] + " 0\n" + instruction_set[12] + " 17\n  " + instruction_set[8] + " 10\n  " + \
                     instruction_set[4] + " b\n  " + instruction_set[1] + "  b\n  " + instruction_set[0] + "  a\n  " + \
                     instruction_set[7] + " 10\n  " + instruction_set[1] + "  a\n" + instruction_set[10] + " 7\n" + \
                     instruction_set[3] + " b\n" + instruction_set[14]
    code_sum_a_to_b_with_loop = "# Summe a bis b\n# mit Schleife\n\ndef a = @34\ndef b = @35\ndef c = @36\n\n" + instruction_set[2] + "  a\n" + \
                                instruction_set[2] + "  b\n" + instruction_set[0] + "  b\n" + instruction_set[4] + " 1\n" + \
                                instruction_set[1] + "  b\n" + instruction_set[0] + "  a\n" + instruction_set[9] + " b\n" + \
                                instruction_set[12] + " 22\n  " + instruction_set[4] + " c\n  " + instruction_set[1] + "  c\n  " + \
                                instruction_set[0] + "  a\n  " + instruction_set[4] + " 1\n  " + instruction_set[1] + "  a\n" + \
                                instruction_set[10] + " 13\n" + instruction_set[3] + " c\n" + instruction_set[14]
    code_sum_a_to_b_without_loop = "# Summe a bis b\n# ohne Schleife\n\ndef a = @38\ndef b = @39\n\n" + instruction_set[2] + "  a\n" + \
                                   instruction_set[2] + "  b\n" + instruction_set[0] + "  a\n" + instruction_set[5] + " 1\n" + \
                                   instruction_set[6] + " a\n" + instruction_set[1] + "  a\n" + instruction_set[7] + " 2\n" + \
                                   instruction_set[1] + "  a\n" + instruction_set[0] + "  b\n" + instruction_set[4] + " 1\n" + \
                                   instruction_set[6] + " b\n" + instruction_set[1] + "  b\n" + instruction_set[7] + " 2\n" + \
                                   instruction_set[1] + "  b\n" + instruction_set[5] + " a\n" + instruction_set[1] + "  a\n" + \
                                   instruction_set[3] + " a\n" + instruction_set[14]
    code_mean_value_3_numbers = "# Durchschnitt\n# dreier Zahlen\n\ndef a = @30\ndef b = @31\n\n" + instruction_set[2] + "  a\n" + \
                                instruction_set[2] + "  b\n" + instruction_set[0] + "  a\n" + instruction_set[4] + " b\n" + \
                                instruction_set[1] + "  a\n" + instruction_set[2] + "  b\n" + instruction_set[0] + "  a\n" + \
                                instruction_set[4] + " b\n" + instruction_set[1] + "  a\n" + instruction_set[0] + "  a\n" + \
                                instruction_set[7] + " 3\n" + instruction_set[1] + "  a\n" + instruction_set[3] + " a\n" + instruction_set[14]
    code_mean_value_arbitrary = "# Durchschnitt\n# beliebig\n# vieler Zahlen\n\ndef a = @32\ndef b = @33\ndef c = @34\ndef anzahl = 5\n\n" + \
                                instruction_set[0] + "  c\n" + instruction_set[9] + " anzahl\n" + instruction_set[12] + " 20\n  " + \
                                instruction_set[2] + "  a\n  " + instruction_set[4] + " b\n  " + instruction_set[1] + "  b\n  " + \
                                instruction_set[0] + "  c\n  " + instruction_set[4] + " 1\n  " + instruction_set[1] + "  c\n" + \
                                instruction_set[10] + " 10\n" + instruction_set[0] + "  b\n" + instruction_set[7] + " anzahl\n" + \
                                instruction_set[1] + "  b\n" + instruction_set[3] + " b\n" + instruction_set[14]


def show_dialog_ram():
    """
    Fenster, um auszuwählen, wie viele Speicherzellen im Speicherwerk (GUI) angezeigt werden.
    """
    global cell_number
    dialog_speicher = QDialog(flags=Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint)
    ui2 = Ui_Dialog_Speicher()
    ui2.setupUi(dialog_speicher)
    ui2.buttonBox.button(QDialogButtonBox.Cancel).setText("Abbrechen")
    ui2.spinBox.setValue(cell_number)
    dialog_speicher.show()
    if dialog_speicher.exec_() == 1 and 1 < int(ui2.spinBox.text()) < ui2.spinBox.maximum() + 1:
        cell_number = int(ui2.spinBox.text())
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        if ui.Speicher.rowCount() * 2 < cell_number:
            while ui.Speicher.rowCount() * 2 < cell_number:
                ui.Speicher.insertRow(ui.Speicher.rowCount())
                it1 = QTableWidgetItem(str((ui.Speicher.rowCount() - 1) * 2))
                it1.setFont(font)
                it2 = QTableWidgetItem(str((ui.Speicher.rowCount() - 1) * 2 + 1))
                it2.setFont(font)
                ui.Speicher.setItem(ui.Speicher.rowCount() - 1, 0, it1)
                ui.Speicher.setItem(ui.Speicher.rowCount() - 1, 1, QTableWidgetItem("0"))
                ui.Speicher.setItem(ui.Speicher.rowCount() - 1, 2, it2)
                ui.Speicher.setItem(ui.Speicher.rowCount() - 1, 3, QTableWidgetItem("0"))

        elif ui.Speicher.rowCount() * 2 > cell_number:
            while ui.Speicher.rowCount() * 2 > cell_number:
                ui.Speicher.removeRow(ui.Speicher.rowCount() - 1)


def show_dialog_info():
    """
    Fenster, in dem Infos über das Programm stehen
    """
    info = QMessageBox()
    info.setIcon(QMessageBox.Information)
    info.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint)
    font = QFont()
    font.setPointSize(10)
    info.setFont(font)
    info.setText("Dieses Programm ist im Rahmen meiner Seminararbeit entstanden.\n"
                 "Die Inspiration bzw. Vorlage stammt vom Modellrechner MOPS.\n"
                 "Die Umsetzung stammt allerdings von mir selbst.\nSteve Heilenz")
    info.setWindowTitle("Info")
    info.setInformativeText("Sprache:     Python 3.7\nIDE:            PyCharm (Community Edition)\n"
                            "für die GUI: PyQt5 und Qt Designer (Open Source Lizenz)\n")
    info.exec_()


def show_dialog_ins_set():
    """
    Fenster, um den Befehlssatz zu verändern
    """
    dialog_inset = QDialog(flags=Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint)
    ui3 = Ui_QDialog_inset()
    ui3.setupUi(dialog_inset)
    get_instruction_set("instruction_set.txt")
    ui3.textEdit.insertPlainText(instruction_set_text)
    ui3.buttonBox.button(QDialogButtonBox.Cancel).setText("Abbrechen")
    ui3.pushButton.clicked.connect(lambda: instruction_set_default())
    dialog_inset.show()

    def instruction_set_default():
        """
        Fenster, um zu bestätigen, dass der Standardbefehlssatz wiederhergestellt werden soll
        """
        dialog_default = QDialog(flags=Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint)
        ui4 = Ui_Dialog()
        ui4.setupUi(dialog_default)
        ui4.buttonBox.button(QDialogButtonBox.Yes).setText("Ja")
        ui4.buttonBox.button(QDialogButtonBox.No).setText("Nein")
        dialog_default.show()
        if dialog_default.exec_() == 1:
            ui3.textEdit.clear()
            ui3.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict."
                                 "dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\np, li "
                                 "{ white-space: pre-wrap; }\n</style></head><body style=\" font-family:\'Consolas\'; font-size:"
                                 "14pt; font-weight:600; font-style:normal;\">\n<p style=\"-qt-paragraph-type:empty; margin-top:"
                                 "0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px"
                                 "; line-height:114%;\"><br /></p></body></html>")
            ui3.textEdit.insertPlainText("ld\nst\nin\nout\nadd\nsub\nmul\ndiv\nmod\ncmp\njmp\njlt\njeq\njgt\nend")

    if dialog_inset.exec_() == 1:
        set_lines = set()
        for line in ui3.textEdit.toPlainText().splitlines(False):
            line = line.replace("\n", "")
            if not line.isspace() and line != "" and not line.strip().__contains__(" ") and not line.strip().__contains__("\t"):
                set_lines.add(line.strip())

        if len(set_lines) == 15:
            with open("instruction_set.txt", "w") as f:
                f.write(ui3.textEdit.toPlainText().replace(" ", ""))
            get_instruction_set("instruction_set.txt")
            setup_demo()

        else:
            info = QMessageBox()
            info.setIcon(QMessageBox.Information)
            info.setWindowFlags(Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint)
            font = QFont()
            font.setPointSize(10)
            info.setFont(font)
            info.setText("Der Befehlssatz wurde nicht geändert!")
            info.setWindowTitle("Fehler")
            info.exec_()


def show_dialog_open():
    """
    Fenster, um zu bestätigen, dass nicht gespeicherter Quellcode beim Öffnen verloren geht
    """
    dialog_o = QFileDialog()
    try:
        global saved, current_file
        dialog = QDialog(flags=Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint)
        ui4 = Ui_Dialog()
        ui4.setupUi(dialog)
        ui4.label.setText("Nicht gespeicherter Quellcode wird verloren gehen!")
        ui4.label_2.setText("")
        dialog.setWindowTitle("Warnung")
        ui4.buttonBox.button(QDialogButtonBox.Yes).setText("Fortfahren")
        ui4.buttonBox.button(QDialogButtonBox.No).setText("Abrechen")
        dialog.show()
        if dialog.exec_() == 1:
            file_name, _ = QFileDialog.getOpenFileName(
                dialog_o, "Öffnen", current_file, "Textdokument (*.txt)")
            with open(file_name, "r") as f:
                ui.Editor.setPlainText(f.read())

            current_file = file_name
    except:
        pass


def show_dialog_save_as():
    """
    Dialogfenster "Speichern als"
    """
    dialog_s = QFileDialog()
    try:
        global saved, current_file, prev_current_file
        file_name, _ = QFileDialog.getSaveFileName(
            dialog_s, "Speichern", current_file, "Textdokument (*.txt)")
        with open(file_name, "w") as f:
            f.write(ui.Editor.toPlainText())

        saved = True
        current_file = file_name
        prev_current_file = file_name
    except:
        pass


def save():
    """
    Speichert den Quellcode in einer Textdatei. Falls der aktuelle Quellcode nicht gespeichert wurde und sich
    die Textdatei geändert hat, mit der gearbeitet wird, wird der Dialog "Speichern als" angezeigt.
    """
    if current_file != prev_current_file and not saved:
        show_dialog_save_as()
    else:
        try:
            with open(current_file, "w") as f:
                f.write(ui.Editor.toPlainText())
        except:
            pass


def new():
    """
    Erstellt eine neue Textdatei für den Quellcode.
    """
    global saved, current_file
    dialog = QDialog(flags=Qt.WindowTitleHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint)
    ui4 = Ui_Dialog()
    ui4.setupUi(dialog)
    ui4.label.setText("Nicht gespeicherter Quellcode wird verloren gehen!")
    ui4.label_2.setText("")
    dialog.setWindowTitle("Warnung")
    ui4.buttonBox.button(QDialogButtonBox.Yes).setText("Fortfahren")
    ui4.buttonBox.button(QDialogButtonBox.No).setText("Abrechen")
    dialog.show()
    if dialog.exec_() == 1:
        current_file = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
        saved = False
        ui.Editor.clear()


def open_doc():
    """
    Öffnet die Dokumentation in der Standard-App für .pdf-Dateien.
    """
    try:
        os.startfile("Dokumentation.pdf")
    except:
        message_box_errors(["Fehler beim Öffnen der Dokumentation!"])


def validate_action(action: QAction):
    """
    Beim Auswählen eines neuen Ablaufs wird der aktuell angewählte Ablauf abgewählt und der Timer wird entsprechend gesetzt.
    """
    if not action.isChecked():
        action.setChecked(True)
    else:
        for a in ui.menuVollst_ndig.actions():
            if a is not action:
                a.setChecked(False)
        ui.actionVNPhasen.setChecked(False)

        if action is ui.actionVNPhasen:
            for a in ui.menuVollst_ndig.actions():
                a.setChecked(False)
            ui.actionVNPhasen.setChecked(True)

        global interval
        if action is ui.actionVNPhasen:
            interval = -1
        else:
            interval = int(action.text().replace("s", ""))


def input_pressed():
    """
    Wird ausgeführt, wenn im Eingaberegister "ENTER" gedrückt wird. Setzt das Programm nach Warten auf die Eingabe fort.
    """
    text = ui.input_reg.text()
    adr = int(ui.input_reg.placeholderText().replace("@", ""))
    cu.CACHE.write(adr, text)
    cu.ALU.acc = text

    try:
        column = 1 if int(cu.register[1].replace("@", "")) % 2 == 0 else 3
        ui.Speicher.setItem(int(adr / 2), column, QTableWidgetItem(text))
    except:
        pass

    if interval < 0:
        ui.button_weiter.setEnabled(True)
        ui.button_weiter.setFocus()
    else:
        timer.setInterval(int(interval * 1000 / 3))

    timer.start()
    ui.input_reg.setPlaceholderText("")
    ui.input_reg.setText("")
    ui.input_reg.setEnabled(False)


def set_saved(new_val: bool):
    global saved
    saved = new_val


# ======================================================================================= #
# ================================= setup =============================================== #


get_instruction_set("instruction_set.txt")
setup_ram(64)
setup_demo()

# === Alle Buttons bzw. klickbare Felder werden mit den dazugehörigen Methoden verknüpft. === #

# Hilfe
ui.actionDokumentation.triggered.connect(lambda: open_doc())
ui.actionInfo.triggered.connect(lambda: show_dialog_info())

# Optionen
ui.actionBefehlssatz_anpassen.triggered.connect(lambda: show_dialog_ins_set())
ui.actionZahl_der_angezeigten_Speicherzellen_2.triggered.connect(lambda: show_dialog_ram())

# Demo
ui.actionFakult_t.triggered.connect(lambda: ui.Editor.setPlainText(code_factorial))
ui.actionFakult_t.triggered.connect(lambda: set_saved(False))
ui.actionQuersumme.triggered.connect(lambda: ui.Editor.setPlainText(code_digit_sum))
ui.actionQuersumme.triggered.connect(lambda: set_saved(False))
ui.actionSumme_a_bis_b_mit_Schleife.triggered.connect(lambda: ui.Editor.setPlainText(code_sum_a_to_b_with_loop))
ui.actionSumme_a_bis_b_mit_Schleife.triggered.connect(lambda: set_saved(False))
ui.actionSumme_a_bis_b_ohne_Schleife.triggered.connect(lambda: ui.Editor.setPlainText(code_sum_a_to_b_without_loop))
ui.actionSumme_a_bis_b_ohne_Schleife.triggered.connect(lambda: set_saved(False))
ui.actionDurchschnitt_dreier_Zahlen_floor.triggered.connect(lambda: ui.Editor.setPlainText(code_mean_value_3_numbers))
ui.actionDurchschnitt_dreier_Zahlen_floor.triggered.connect(lambda: set_saved(False))
ui.actionDurchschnitt_beliebig_vieler_Zahlen.triggered.connect(lambda: ui.Editor.setPlainText(code_mean_value_arbitrary))
ui.actionDurchschnitt_beliebig_vieler_Zahlen.triggered.connect(lambda: set_saved(False))

# Datei
ui.actionNeu.triggered.connect(lambda: new())
ui.action_ffnen.triggered.connect(lambda: show_dialog_open())
ui.actionSpeichern.triggered.connect(lambda: save())
ui.actionSpeichernAls.triggered.connect(lambda: show_dialog_save_as())

# Ablauf
ui.action0s.triggered.connect(lambda: validate_action(ui.action0s))
ui.action1s.triggered.connect(lambda: validate_action(ui.action1s))
ui.action2s.triggered.connect(lambda: validate_action(ui.action2s))
ui.action3s.triggered.connect(lambda: validate_action(ui.action3s))
ui.action4s.triggered.connect(lambda: validate_action(ui.action4s))
ui.action5s.triggered.connect(lambda: validate_action(ui.action5s))
ui.action10s.triggered.connect(lambda: validate_action(ui.action10s))
ui.actionVNPhasen.triggered.connect(lambda: validate_action(ui.actionVNPhasen))

# Sonstiges
ui.Editor.textChanged.connect(lambda: set_saved(False))
ui.input_reg.setValidator(QRegExpValidator(QRegExp("^-?\d*\d+$")))
ui.input_reg.returnPressed.connect(lambda: input_pressed())
ui.button_start.clicked.connect(lambda: start())
ui.button_stop.clicked.connect(lambda: stop())
ui.button_weiter.clicked.connect(lambda: run_vn())
ui.Speicher.setStyleSheet("alternate-background-color: white;background-color: gainsboro;")

ui.Editor.setFocus()
main_window.show()
sys.exit(app.exec_())
