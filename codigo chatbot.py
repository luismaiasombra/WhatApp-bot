
#ifndef CHATBOTHP1276_H
#define CHATBOTHP1276_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QFrame>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QSpacerItem>
#include <QtGui/QStackedWidget>
#include <QtGui/QStatusBar>
#include <QtGui/QTabWidget>
#include <QtGui/QTableWidget>
#include <QtGui/QToolBox>
#include <QtGui/QVBoxLayout>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout;
    QFrame *sub_container;
    QVBoxLayout *verticalLayout_2;
    QFrame *frame_5;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_3;
    QFrame *frame_6;
    QVBoxLayout *verticalLayout_3;
    QToolBox *toolBox;
    QWidget *page;
    QVBoxLayout *verticalLayout_4;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QPushButton *pushButton_4;
    QSpacerItem *verticalSpacer;
    QWidget *page_2;
    QFrame *frame_2;
    QVBoxLayout *verticalLayout;
    QFrame *frame;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *pushButton;
    QLabel *label;
    QFrame *frame_3;
    QVBoxLayout *verticalLayout_5;
    QStackedWidget *Pages;
    QWidget *page_home;
    QWidget *Historico;
    QVBoxLayout *verticalLayout_7;
    QTabWidget *tabWidget;
    QWidget *tab;
    QWidget *tab_2;
    QTableWidget *tableWidget;
    QFrame *frame_7;
    QVBoxLayout *verticalLayout_8;
    QCheckBox *checkBox;
    QCheckBox *checkBox_2;
    QCheckBox *checkBox_3;
    QCheckBox *checkBox_4;
    QPushButton *pushButton_5;
    QWidget *Avisos;
    QWidget *page_5;
    QVBoxLayout *verticalLayout_6;
    QLabel *Logo;
    QFrame *frame_4;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_2;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(862, 486);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        horizontalLayout = new QHBoxLayout(centralwidget);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        sub_container = new QFrame(centralwidget);
        sub_container->setObjectName(QString::fromUtf8("sub_container"));
        sub_container->setMaximumSize(QSize(200, 16777215));
        sub_container->setFrameShape(QFrame::StyledPanel);
        sub_container->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(sub_container);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        frame_5 = new QFrame(sub_container);
        frame_5->setObjectName(QString::fromUtf8("frame_5"));
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        horizontalLayout_4 = new QHBoxLayout(frame_5);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        label_3 = new QLabel(frame_5);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout_4->addWidget(label_3);


        verticalLayout_2->addWidget(frame_5);

        frame_6 = new QFrame(sub_container);
        frame_6->setObjectName(QString::fromUtf8("frame_6"));
        frame_6->setFrameShape(QFrame::StyledPanel);
        frame_6->setFrameShadow(QFrame::Raised);
        verticalLayout_3 = new QVBoxLayout(frame_6);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        toolBox = new QToolBox(frame_6);
        toolBox->setObjectName(QString::fromUtf8("toolBox"));
        page = new QWidget();
        page->setObjectName(QString::fromUtf8("page"));
        page->setGeometry(QRect(0, 0, 160, 294));
        verticalLayout_4 = new QVBoxLayout(page);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        pushButton_2 = new QPushButton(page);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        verticalLayout_4->addWidget(pushButton_2);

        pushButton_3 = new QPushButton(page);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));

        verticalLayout_4->addWidget(pushButton_3);

        pushButton_4 = new QPushButton(page);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));

        verticalLayout_4->addWidget(pushButton_4);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer);

        toolBox->addItem(page, QString::fromUtf8("Page 1"));
        page_2 = new QWidget();
        page_2->setObjectName(QString::fromUtf8("page_2"));
        page_2->setGeometry(QRect(0, 0, 160, 294));
        toolBox->addItem(page_2, QString::fromUtf8("Page 2"));

        verticalLayout_3->addWidget(toolBox);


        verticalLayout_2->addWidget(frame_6);


        horizontalLayout->addWidget(sub_container);

        frame_2 = new QFrame(centralwidget);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(frame_2);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        frame = new QFrame(frame_2);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(frame);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        pushButton = new QPushButton(frame);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        horizontalLayout_2->addWidget(pushButton);

        label = new QLabel(frame);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);


        verticalLayout->addWidget(frame);

        frame_3 = new QFrame(frame_2);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(frame_3->sizePolicy().hasHeightForWidth());
        frame_3->setSizePolicy(sizePolicy);
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        verticalLayout_5 = new QVBoxLayout(frame_3);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        Pages = new QStackedWidget(frame_3);
        Pages->setObjectName(QString::fromUtf8("Pages"));
        page_home = new QWidget();
        page_home->setObjectName(QString::fromUtf8("page_home"));
        Pages->addWidget(page_home);
        Historico = new QWidget();
        Historico->setObjectName(QString::fromUtf8("Historico"));
        verticalLayout_7 = new QVBoxLayout(Historico);
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        tabWidget = new QTabWidget(Historico);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        tabWidget->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        tableWidget = new QTableWidget(tab_2);
        tableWidget->setObjectName(QString::fromUtf8("tableWidget"));
        tableWidget->setGeometry(QRect(10, 20, 341, 192));
        frame_7 = new QFrame(tab_2);
        frame_7->setObjectName(QString::fromUtf8("frame_7"));
        frame_7->setGeometry(QRect(410, 29, 90, 106));
        frame_7->setFrameShape(QFrame::StyledPanel);
        frame_7->setFrameShadow(QFrame::Raised);
        verticalLayout_8 = new QVBoxLayout(frame_7);
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        checkBox = new QCheckBox(frame_7);
        checkBox->setObjectName(QString::fromUtf8("checkBox"));
        QFont font;
        font.setFamily(QString::fromUtf8("Roboto"));
        font.setPointSize(10);
        checkBox->setFont(font);
        checkBox->setIconSize(QSize(18, 18));

        verticalLayout_8->addWidget(checkBox);

        checkBox_2 = new QCheckBox(frame_7);
        checkBox_2->setObjectName(QString::fromUtf8("checkBox_2"));
        checkBox_2->setFont(font);

        verticalLayout_8->addWidget(checkBox_2);

        checkBox_3 = new QCheckBox(frame_7);
        checkBox_3->setObjectName(QString::fromUtf8("checkBox_3"));
        checkBox_3->setFont(font);
        checkBox_3->setIconSize(QSize(18, 18));

        verticalLayout_8->addWidget(checkBox_3);

        checkBox_4 = new QCheckBox(frame_7);
        checkBox_4->setObjectName(QString::fromUtf8("checkBox_4"));
        checkBox_4->setFont(font);
        checkBox_4->setIconSize(QSize(18, 18));

        verticalLayout_8->addWidget(checkBox_4);

        pushButton_5 = new QPushButton(tab_2);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));
        pushButton_5->setGeometry(QRect(420, 180, 75, 23));
        tabWidget->addTab(tab_2, QString());

        verticalLayout_7->addWidget(tabWidget);

        Pages->addWidget(Historico);
        Avisos = new QWidget();
        Avisos->setObjectName(QString::fromUtf8("Avisos"));
        Pages->addWidget(Avisos);
        page_5 = new QWidget();
        page_5->setObjectName(QString::fromUtf8("page_5"));
        verticalLayout_6 = new QVBoxLayout(page_5);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        Logo = new QLabel(page_5);
        Logo->setObjectName(QString::fromUtf8("Logo"));

        verticalLayout_6->addWidget(Logo);

        Pages->addWidget(page_5);

        verticalLayout_5->addWidget(Pages);


        verticalLayout->addWidget(frame_3);

        frame_4 = new QFrame(frame_2);
        frame_4->setObjectName(QString::fromUtf8("frame_4"));
        frame_4->setFrameShape(QFrame::StyledPanel);
        frame_4->setFrameShadow(QFrame::Raised);
        horizontalLayout_3 = new QHBoxLayout(frame_4);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label_2 = new QLabel(frame_4);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_3->addWidget(label_2);


        verticalLayout->addWidget(frame_4);


        horizontalLayout->addWidget(frame_2);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 862, 21));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        toolBox->setCurrentIndex(0);
        Pages->setCurrentIndex(1);
        tabWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("MainWindow", "TextLabel", 0, QApplication::UnicodeUTF8));
        pushButton_2->setText(QApplication::translate("MainWindow", "Historico", 0, QApplication::UnicodeUTF8));
        pushButton_3->setText(QApplication::translate("MainWindow", "Avisos", 0, QApplication::UnicodeUTF8));
        pushButton_4->setText(QApplication::translate("MainWindow", "Planilhas", 0, QApplication::UnicodeUTF8));
        toolBox->setItemText(toolBox->indexOf(page), QApplication::translate("MainWindow", "Page 1", 0, QApplication::UnicodeUTF8));
        toolBox->setItemText(toolBox->indexOf(page_2), QApplication::translate("MainWindow", "Page 2", 0, QApplication::UnicodeUTF8));
        pushButton->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "TextLabel", 0, QApplication::UnicodeUTF8));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("MainWindow", "Historico", 0, QApplication::UnicodeUTF8));
        checkBox->setText(QApplication::translate("MainWindow", "Semente", 0, QApplication::UnicodeUTF8));
        checkBox_2->setText(QApplication::translate("MainWindow", "Bronze", 0, QApplication::UnicodeUTF8));
        checkBox_3->setText(QApplication::translate("MainWindow", "Prata", 0, QApplication::UnicodeUTF8));
        checkBox_4->setText(QApplication::translate("MainWindow", "Ouro", 0, QApplication::UnicodeUTF8));
        pushButton_5->setText(QApplication::translate("MainWindow", "Enviar", 0, QApplication::UnicodeUTF8));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("MainWindow", "Mensagens", 0, QApplication::UnicodeUTF8));
        Logo->setText(QApplication::translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/Icons/logo menor.png\"/></p></body></html>", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "TextLabel", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // CHATBOTHP1276_H
