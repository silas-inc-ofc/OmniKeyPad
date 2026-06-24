import tkinter as tk
from tkinter import font as tkfont
import pyperclip
from itertools import *

# ── Character groups ──────────────────────────────────────────────────────────


length_units = []



Si_units = f'QRYZEPTGMkhdcmμnpfazyrq'
length_bases = ['m','in','ft','yd','nm','LD','R🜨','ly','AU','pc','re','λC','a0','lp','ls',
                'lQCD','R☉','R☽','R☿','R♀','R♂','R♃','R♄','R⛢','R♆','R⯔','R⚳',
                'R⚴','R⚵','R⚶','R⯙','R⯚','R⚷','R⯛','R⯜','R⯱','R⯲','R❈','R🌀','Å','xu','Å*',
                ]

nuclides = ['¹H', '²H', '³H', '⁴H', '⁵H', '⁶H', '⁷H', '²He', '³He', '⁴He', '⁵He', '⁶He', '⁷He', '⁸He', '⁹He', '¹⁰He', '³Li', '⁴Li', '⁵Li', '⁶Li', '⁷Li',
            '⁸Li', '⁹Li', '¹⁰Li', '¹¹Li', '¹²Li', '⁵Be', '⁶Be', '⁷Be', '⁸Be', '⁹Be', '¹⁰Be', '¹¹Be', '¹²Be', '¹³Be', '¹⁴Be', '¹⁵Be', '¹⁶Be', '⁶B', '⁷B', '⁸B',
            '⁹B', '¹⁰B', '¹¹B', '¹²B', '¹³B', '¹⁴B', '¹⁵B', '¹⁶B', '¹⁷B', '¹⁸B', '¹⁹B', '⁸C', '⁹C', '¹⁰C', '¹¹C', '¹²C', '¹³C', '¹⁴C', '¹⁵C', '¹⁶C', '¹⁷C', '¹⁸C',
            '¹⁹C', '²⁰C', '²¹C', '²²C', '¹⁰N', '¹¹N', '¹²N', '¹³N', '¹⁴N', '¹⁵N', '¹⁶N', '¹⁷N', '¹⁸N', '¹⁹N', '²⁰N', '²¹N', '²²N', '²³N', '²⁴N', '²⁵N', '¹²O', '¹³O',
            '¹⁴O', '¹⁵O', '¹⁶O', '¹⁷O', '¹⁸O', '¹⁹O', '²⁰O', '²¹O', '²²O', '²³O', '²⁴O', '²⁵O', '²⁶O', '²⁷O', '²⁸O', '¹⁴F', '¹⁵F', '¹⁶F', '¹⁷F', '¹⁸F', '¹⁹F', '²⁰F', '²¹F',
            '²²F', '²³F', '²⁴F', '²⁵F', '²⁶F', '²⁷F', '²⁸F', '²⁹F', '³⁰F', '³¹F', '¹⁶Ne', '¹⁷Ne', '¹⁸Ne', '¹⁹Ne', '²⁰Ne', '²¹Ne', '²²Ne', '²³Ne', '²⁴Ne', '²⁵Ne', '²⁶Ne', '²⁷Ne',
            '²⁸Ne', '²⁹Ne', '³⁰Ne', '³¹Ne', '³²Ne', '³³Ne', '³⁴Ne', '¹⁸Na', '¹⁹Na', '²⁰Na', '²¹Na', '²²Na', '²³Na', '²⁴Na', '²⁵Na', '²⁶Na', '²⁷Na', '²⁸Na', '²⁹Na', '³⁰Na', '³¹Na',
            '³²Na', '³³Na', '³⁴Na', '³⁵Na', '³⁶Na', '³⁷Na', '¹⁹Mg', '²⁰Mg', '²¹Mg', '²²Mg', '²³Mg', '²⁴Mg', '²⁵Mg', '²⁶Mg', '²⁷Mg', '²⁸Mg', '²⁹Mg', '³⁰Mg', '³¹Mg', '³²Mg', '³³Mg',
            '³⁴Mg', '³⁵Mg', '³⁶Mg', '³⁷Mg', '³⁸Mg', '³⁹Mg', '⁴⁰Mg', '²¹Al', '²²Al', '²³Al', '²⁴Al', '²⁵Al', '²⁶Al', '²⁷Al', '²⁸Al', '²⁹Al', '³⁰Al', '³¹Al', '³²Al', '³³Al', '³⁴Al',
            '³⁵Al', '³⁶Al', '³⁷Al', '³⁸Al', '³⁹Al', '⁴⁰Al', '⁴¹Al', '⁴²Al', '²²Si', '²³Si', '²⁴Si', '²⁵Si', '²⁶Si', '²⁷Si', '²⁸Si', '²⁹Si', '³⁰Si', '³¹Si', '³²Si', '³³Si', '³⁴Si',
            '³⁵Si', '³⁶Si', '³⁷Si', '³⁸Si', '³⁹Si', '⁴⁰Si', '⁴¹Si', '⁴²Si', '⁴³Si', '⁴⁴Si', '²⁴P', '²⁵P', '²⁶P', '²⁷P', '²⁸P', '²⁹P', '³⁰P', '³¹P', '³²P', '³³P', '³⁴P', '³⁵P', '³⁶P',
            '³⁷P', '³⁸P', '³⁹P', '⁴⁰P', '⁴¹P', '⁴²P', '⁴³P', '⁴⁴P', '⁴⁵P', '⁴⁶P', '²⁶S', '²⁷S', '²⁸S', '²⁹S', '³⁰S', '³¹S', '³²S', '³³S', '³⁴S', '³⁵S', '³⁶S', '³⁷S', '³⁸S', '³⁹S', '⁴⁰S',
            '⁴¹S', '⁴²S', '⁴³S', '⁴⁴S', '⁴⁵S', '⁴⁶S', '⁴⁷S', '⁴⁸S', '⁴⁹S', '²⁸Cl', '²⁹Cl', '³⁰Cl', '³¹Cl', '³²Cl', '³³Cl', '³⁴Cl', '³⁵Cl', '³⁶Cl', '³⁷Cl', '³⁸Cl', '³⁹Cl', '⁴⁰Cl', '⁴¹Cl',
            '⁴²Cl', '⁴³Cl', '⁴⁴Cl', '⁴⁵Cl', '⁴⁶Cl', '⁴⁷Cl', '⁴⁸Cl', '⁴⁹Cl', '⁵⁰Cl', '⁵¹Cl', '³⁰Ar', '³¹Ar', '³²Ar', '³³Ar', '³⁴Ar', '³⁵Ar', '³⁶Ar', '³⁷Ar', '³⁸Ar', '³⁹Ar', '⁴⁰Ar', '⁴¹Ar',
            '⁴²Ar', '⁴³Ar', '⁴⁴Ar', '⁴⁵Ar', '⁴⁶Ar', '⁴⁷Ar', '⁴⁸Ar', '⁴⁹Ar', '⁵⁰Ar', '⁵¹Ar', '⁵²Ar', '⁵³Ar', '³²K', '³³K', '³⁴K', '³⁵K', '³⁶K', '³⁷K', '³⁸K', '³⁹K', '⁴⁰K', '⁴¹K', '⁴²K',
            '⁴³K', '⁴⁴K', '⁴⁵K', '⁴⁶K', '⁴⁷K', '⁴⁸K', '⁴⁹K', '⁵⁰K', '⁵¹K', '⁵²K', '⁵³K', '⁵⁴K', '⁵⁵K', '³⁴Ca', '³⁵Ca', '³⁶Ca', '³⁷Ca', '³⁸Ca', '³⁹Ca', '⁴⁰Ca', '⁴¹Ca', '⁴²Ca', '⁴³Ca',
            '⁴⁴Ca', '⁴⁵Ca', '⁴⁶Ca', '⁴⁷Ca', '⁴⁸Ca', '⁴⁹Ca', '⁵⁰Ca', '⁵¹Ca', '⁵²Ca', '⁵³Ca', '⁵⁴Ca', '⁵⁵Ca', '⁵⁶Ca', '⁵⁷Ca', '³⁶Sc', '³⁷Sc', '³⁸Sc', '³⁹Sc', '⁴⁰Sc', '⁴¹Sc', '⁴²Sc',
            '⁴³Sc', '⁴⁴Sc', '⁴⁵Sc', '⁴⁶Sc', '⁴⁷Sc', '⁴⁸Sc', '⁴⁹Sc', '⁵⁰Sc', '⁵¹Sc', '⁵²Sc', '⁵³Sc', '⁵⁴Sc', '⁵⁵Sc', '⁵⁶Sc', '⁵⁷Sc', '⁵⁸Sc', '⁵⁹Sc', '⁶⁰Sc', '³⁸Ti', '³⁹Ti', '⁴⁰Ti',
            '⁴¹Ti', '⁴²Ti', '⁴³Ti', '⁴⁴Ti', '⁴⁵Ti', '⁴⁶Ti', '⁴⁷Ti', '⁴⁸Ti', '⁴⁹Ti', '⁵⁰Ti', '⁵¹Ti', '⁵²Ti', '⁵³Ti', '⁵⁴Ti', '⁵⁵Ti', '⁵⁶Ti', '⁵⁷Ti', '⁵⁸Ti', '⁵⁹Ti', '⁶⁰Ti', '⁶¹Ti',
            '⁶²Ti', '⁶³Ti', '⁴⁰V', '⁴¹V', '⁴²V', '⁴³V', '⁴⁴V', '⁴⁵V', '⁴⁶V', '⁴⁷V', '⁴⁸V', '⁴⁹V', '⁵⁰V', '⁵¹V', '⁵²V', '⁵³V', '⁵⁴V', '⁵⁵V', '⁵⁶V', '⁵⁷V', '⁵⁸V', '⁵⁹V', '⁶⁰V', '⁶¹V',
            '⁶²V', '⁶³V', '⁶⁴V', '⁶⁵V', '⁴²Cr', '⁴³Cr', '⁴⁴Cr', '⁴⁵Cr', '⁴⁶Cr', '⁴⁷Cr', '⁴⁸Cr', '⁴⁹Cr', '⁵⁰Cr', '⁵¹Cr', '⁵²Cr', '⁵³Cr', '⁵⁴Cr', '⁵⁵Cr', '⁵⁶Cr', '⁵⁷Cr', '⁵⁸Cr',
            '⁵⁹Cr', '⁶⁰Cr', '⁶¹Cr', '⁶²Cr', '⁶³Cr', '⁶⁴Cr', '⁶⁵Cr', '⁶⁶Cr', '⁶⁷Cr', '⁴⁴Mn', '⁴⁵Mn', '⁴⁶Mn', '⁴⁷Mn', '⁴⁸Mn', '⁴⁹Mn', '⁵⁰Mn', '⁵¹Mn', '⁵²Mn', '⁵³Mn', '⁵⁴Mn', '⁵⁵Mn',
            '⁵⁶Mn', '⁵⁷Mn', '⁵⁸Mn', '⁵⁹Mn', '⁶⁰Mn', '⁶¹Mn', '⁶²Mn', '⁶³Mn', '⁶⁴Mn', '⁶⁵Mn', '⁶⁶Mn', '⁶⁷Mn', '⁶⁸Mn', '⁶⁹Mn', '⁴⁵Fe', '⁴⁶Fe', '⁴⁷Fe', '⁴⁸Fe', '⁴⁹Fe', '⁵⁰Fe', '⁵¹Fe',
            '⁵²Fe', '⁵³Fe', '⁵⁴Fe', '⁵⁵Fe', '⁵⁶Fe', '⁵⁷Fe', '⁵⁸Fe', '⁵⁹Fe', '⁶⁰Fe', '⁶¹Fe', '⁶²Fe', '⁶³Fe', '⁶⁴Fe', '⁶⁵Fe', '⁶⁶Fe', '⁶⁷Fe', '⁶⁸Fe', '⁶⁹Fe', '⁷⁰Fe', '⁷¹Fe', '⁷²Fe',
            '⁴⁷Co', '⁴⁸Co', '⁴⁹Co', '⁵⁰Co', '⁵¹Co', '⁵²Co', '⁵³Co', '⁵⁴Co', '⁵⁵Co', '⁵⁶Co', '⁵⁷Co', '⁵⁸Co', '⁵⁹Co', '⁶⁰Co', '⁶¹Co', '⁶²Co', '⁶³Co', '⁶⁴Co', '⁶⁵Co', '⁶⁶Co', '⁶⁷Co',
            '⁶⁸Co', '⁶⁹Co', '⁷⁰Co', '⁷¹Co', '⁷²Co', '⁷³Co', '⁷⁴Co', '⁷⁵Co', '⁴⁸Ni', '⁴⁹Ni', '⁵⁰Ni', '⁵¹Ni', '⁵²Ni', '⁵³Ni', '⁵⁴Ni', '⁵⁵Ni', '⁵⁶Ni', '⁵⁷Ni', '⁵⁸Ni', '⁵⁹Ni', '⁶⁰Ni',
            '⁶¹Ni', '⁶²Ni', '⁶³Ni', '⁶⁴Ni', '⁶⁵Ni', '⁶⁶Ni', '⁶⁷Ni', '⁶⁸Ni', '⁶⁹Ni', '⁷⁰Ni', '⁷¹Ni', '⁷²Ni', '⁷³Ni', '⁷⁴Ni', '⁷⁵Ni', '⁷⁶Ni', '⁷⁷Ni', '⁷⁸Ni', '⁵²Cu', '⁵³Cu', '⁵⁴Cu',
            '⁵⁵Cu', '⁵⁶Cu', '⁵⁷Cu', '⁵⁸Cu', '⁵⁹Cu', '⁶⁰Cu', '⁶¹Cu', '⁶²Cu', '⁶³Cu', '⁶⁴Cu', '⁶⁵Cu', '⁶⁶Cu', '⁶⁷Cu', '⁶⁸Cu', '⁶⁹Cu', '⁷⁰Cu', '⁷¹Cu', '⁷²Cu', '⁷³Cu', '⁷⁴Cu', '⁷⁵Cu', '⁷⁶Cu', '⁷⁷Cu', '⁷⁸Cu', '⁷⁹Cu', '⁸⁰Cu', '⁵⁴Zn', '⁵⁵Zn', '⁵⁶Zn', '⁵⁷Zn', '⁵⁸Zn', '⁵⁹Zn', '⁶⁰Zn', '⁶¹Zn', '⁶²Zn', '⁶³Zn', '⁶⁴Zn', '⁶⁵Zn', '⁶⁶Zn', '⁶⁷Zn', '⁶⁸Zn', '⁶⁹Zn', '⁷⁰Zn', '⁷¹Zn', '⁷²Zn', '⁷³Zn', '⁷⁴Zn', '⁷⁵Zn', '⁷⁶Zn', '⁷⁷Zn', '⁷⁸Zn', '⁷⁹Zn', '⁸⁰Zn', '⁸¹Zn', '⁸²Zn', '⁸³Zn', '⁵⁶Ga', '⁵⁷Ga', '⁵⁸Ga', '⁵⁹Ga', '⁶⁰Ga', '⁶¹Ga', '⁶²Ga', '⁶³Ga', '⁶⁴Ga', '⁶⁵Ga', '⁶⁶Ga', '⁶⁷Ga', '⁶⁸Ga', '⁶⁹Ga', '⁷⁰Ga', '⁷¹Ga', '⁷²Ga', '⁷³Ga', '⁷⁴Ga', '⁷⁵Ga', '⁷⁶Ga', '⁷⁷Ga', '⁷⁸Ga', '⁷⁹Ga', '⁸⁰Ga', '⁸¹Ga', '⁸²Ga', '⁸³Ga', '⁸⁴Ga', '⁸⁵Ga', '⁸⁶Ga', '⁵⁸Ge', '⁵⁹Ge', '⁶⁰Ge', '⁶¹Ge', '⁶²Ge', '⁶³Ge', '⁶⁴Ge', '⁶⁵Ge', '⁶⁶Ge', '⁶⁷Ge', '⁶⁸Ge', '⁶⁹Ge', '⁷⁰Ge', '⁷¹Ge', '⁷²Ge', '⁷³Ge', '⁷⁴Ge', '⁷⁵Ge', '⁷⁶Ge', '⁷⁷Ge', '⁷⁸Ge', '⁷⁹Ge', '⁸⁰Ge', '⁸¹Ge', '⁸²Ge', '⁸³Ge', '⁸⁴Ge', '⁸⁵Ge', '⁸⁶Ge', '⁸⁷Ge', '⁸⁸Ge', '⁸⁹Ge', '⁶⁰As', '⁶¹As', '⁶²As', '⁶³As', '⁶⁴As', '⁶⁵As', '⁶⁶As', '⁶⁷As', '⁶⁸As', '⁶⁹As', '⁷⁰As', '⁷¹As', '⁷²As', '⁷³As', '⁷⁴As', '⁷⁵As', '⁷⁶As', '⁷⁷As', '⁷⁸As', '⁷⁹As', '⁸⁰As', '⁸¹As', '⁸²As', '⁸³As', '⁸⁴As', '⁸⁵As', '⁸⁶As', '⁸⁷As', '⁸⁸As', '⁸⁹As', '⁹⁰As', '⁹¹As', '⁹²As', '⁶⁵Se', '⁶⁶Se', '⁶⁷Se', '⁶⁸Se', '⁶⁹Se', '⁷⁰Se', '⁷¹Se', '⁷²Se', '⁷³Se', '⁷⁴Se', '⁷⁵Se', '⁷⁶Se', '⁷⁷Se', '⁷⁸Se', '⁷⁹Se', '⁸⁰Se', '⁸¹Se', '⁸²Se', '⁸³Se', '⁸⁴Se', '⁸⁵Se', '⁸⁶Se', '⁸⁷Se', '⁸⁸Se', '⁸⁹Se', '⁹⁰Se', '⁹¹Se', '⁹²Se', '⁹³Se', '⁹⁴Se', '⁶⁷Br', '⁶⁸Br', '⁶⁹Br', '⁷⁰Br', '⁷¹Br', '⁷²Br', '⁷³Br', '⁷⁴Br', '⁷⁵Br', '⁷⁶Br', '⁷⁷Br', '⁷⁸Br', '⁷⁹Br', '⁸⁰Br', '⁸¹Br', '⁸²Br', '⁸³Br', '⁸⁴Br', '⁸⁵Br', '⁸⁶Br', '⁸⁷Br', '⁸⁸Br', '⁸⁹Br', '⁹⁰Br', '⁹¹Br', '⁹²Br', '⁹³Br', '⁹⁴Br', '⁹⁵Br', '⁹⁶Br', '⁹⁷Br', '⁶⁹Kr', '⁷⁰Kr', '⁷¹Kr', '⁷²Kr', '⁷³Kr', '⁷⁴Kr', '⁷⁵Kr', '⁷⁶Kr', '⁷⁷Kr', '⁷⁸Kr', '⁷⁹Kr', '⁸⁰Kr', '⁸¹Kr', '⁸²Kr', '⁸³Kr', '⁸⁴Kr', '⁸⁵Kr', '⁸⁶Kr', '⁸⁷Kr', '⁸⁸Kr', '⁸⁹Kr', '⁹⁰Kr', '⁹¹Kr', '⁹²Kr', '⁹³Kr', '⁹⁴Kr', '⁹⁵Kr', '⁹⁶Kr', '⁹⁷Kr', '⁹⁸Kr', '⁹⁹Kr', '¹⁰⁰Kr', '⁷¹Rb', '⁷²Rb', '⁷³Rb', '⁷⁴Rb', '⁷⁵Rb', '⁷⁶Rb', '⁷⁷Rb', '⁷⁸Rb', '⁷⁹Rb', '⁸⁰Rb', '⁸¹Rb', '⁸²Rb', '⁸³Rb', '⁸⁴Rb', '⁸⁵Rb', '⁸⁶Rb', '⁸⁷Rb', '⁸⁸Rb', '⁸⁹Rb', '⁹⁰Rb', '⁹¹Rb', '⁹²Rb', '⁹³Rb', '⁹⁴Rb', '⁹⁵Rb', '⁹⁶Rb', '⁹⁷Rb', '⁹⁸Rb', '⁹⁹Rb', '¹⁰⁰Rb', '¹⁰¹Rb', '¹⁰²Rb', '⁷³Sr', '⁷⁴Sr', '⁷⁵Sr', '⁷⁶Sr', '⁷⁷Sr', '⁷⁸Sr', '⁷⁹Sr', '⁸⁰Sr', '⁸¹Sr', '⁸²Sr', '⁸³Sr', '⁸⁴Sr', '⁸⁵Sr', '⁸⁶Sr', '⁸⁷Sr', '⁸⁸Sr', '⁸⁹Sr', '⁹⁰Sr', '⁹¹Sr', '⁹²Sr', '⁹³Sr', '⁹⁴Sr', '⁹⁵Sr', '⁹⁶Sr', '⁹⁷Sr', '⁹⁸Sr', '⁹⁹Sr', '¹⁰⁰Sr', '¹⁰¹Sr', '¹⁰²Sr', '¹⁰³Sr', '¹⁰⁴Sr', '¹⁰⁵Sr', '⁷⁶Y', '⁷⁷Y', '⁷⁸Y', '⁷⁹Y', '⁸⁰Y', '⁸¹Y', '⁸²Y', '⁸³Y', '⁸⁴Y', '⁸⁵Y', '⁸⁶Y', '⁸⁷Y', '⁸⁸Y', '⁸⁹Y', '⁹⁰Y', '⁹¹Y', '⁹²Y', '⁹³Y', '⁹⁴Y', '⁹⁵Y', '⁹⁶Y', '⁹⁷Y', '⁹⁸Y', '⁹⁹Y', '¹⁰⁰Y', '¹⁰¹Y', '¹⁰²Y', '¹⁰³Y', '¹⁰⁴Y', '¹⁰⁵Y', '¹⁰⁶Y', '¹⁰⁷Y', '¹⁰⁸Y', '⁷⁸Zr', '⁷⁹Zr', '⁸⁰Zr', '⁸¹Zr', '⁸²Zr', '⁸³Zr', '⁸⁴Zr', '⁸⁵Zr', '⁸⁶Zr', '⁸⁷Zr', '⁸⁸Zr', '⁸⁹Zr', '⁹⁰Zr', '⁹¹Zr', '⁹²Zr', '⁹³Zr', '⁹⁴Zr', '⁹⁵Zr', '⁹⁶Zr', '⁹⁷Zr', '⁹⁸Zr', '⁹⁹Zr', '¹⁰⁰Zr', '¹⁰¹Zr', '¹⁰²Zr', '¹⁰³Zr', '¹⁰⁴Zr', '¹⁰⁵Zr', '¹⁰⁶Zr', '¹⁰⁷Zr', '¹⁰⁸Zr', '¹⁰⁹Zr', '¹¹⁰Zr', '⁸¹Nb', '⁸²Nb', '⁸³Nb', '⁸⁴Nb', '⁸⁵Nb', '⁸⁶Nb', '⁸⁷Nb', '⁸⁸Nb', '⁸⁹Nb', '⁹⁰Nb', '⁹¹Nb', '⁹²Nb', '⁹³Nb', '⁹⁴Nb', '⁹⁵Nb', '⁹⁶Nb', '⁹⁷Nb', '⁹⁸Nb', '⁹⁹Nb', '¹⁰⁰Nb', '¹⁰¹Nb', '¹⁰²Nb', '¹⁰³Nb', '¹⁰⁴Nb', '¹⁰⁵Nb', '¹⁰⁶Nb', '¹⁰⁷Nb', '¹⁰⁸Nb', '¹⁰⁹Nb', '¹¹⁰Nb', '¹¹¹Nb', '¹¹²Nb', '¹¹³Nb', '⁸³Mo', '⁸⁴Mo', '⁸⁵Mo', '⁸⁶Mo', '⁸⁷Mo', '⁸⁸Mo', '⁸⁹Mo', '⁹⁰Mo', '⁹¹Mo', '⁹²Mo', '⁹³Mo', '⁹⁴Mo', '⁹⁵Mo', '⁹⁶Mo', '⁹⁷Mo', '⁹⁸Mo', '⁹⁹Mo', '¹⁰⁰Mo', '¹⁰¹Mo', '¹⁰²Mo', '¹⁰³Mo', '¹⁰⁴Mo', '¹⁰⁵Mo', '¹⁰⁶Mo', '¹⁰⁷Mo', '¹⁰⁸Mo', '¹⁰⁹Mo', '¹¹⁰Mo', '¹¹¹Mo', '¹¹²Mo', '¹¹³Mo', '¹¹⁴Mo', '¹¹⁵Mo', '⁸⁵Tc', '⁸⁶Tc', '⁸⁷Tc', '⁸⁸Tc', '⁸⁹Tc', '⁹⁰Tc', '⁹¹Tc', '⁹²Tc', '⁹³Tc', '⁹⁴Tc', '⁹⁵Tc', '⁹⁶Tc', '⁹⁷Tc', '⁹⁸Tc', '⁹⁹Tc', '¹⁰⁰Tc', '¹⁰¹Tc', '¹⁰²Tc', '¹⁰³Tc', '¹⁰⁴Tc', '¹⁰⁵Tc', '¹⁰⁶Tc', '¹⁰⁷Tc', '¹⁰⁸Tc', '¹⁰⁹Tc', '¹¹⁰Tc', '¹¹¹Tc', '¹¹²Tc', '¹¹³Tc', '¹¹⁴Tc', '¹¹⁵Tc', '¹¹⁶Tc', '¹¹⁷Tc', '¹¹⁸Tc', '⁸⁷Ru', '⁸⁸Ru', '⁸⁹Ru', '⁹⁰Ru', '⁹¹Ru', '⁹²Ru', '⁹³Ru', '⁹⁴Ru', '⁹⁵Ru', '⁹⁶Ru', '⁹⁷Ru', '⁹⁸Ru', '⁹⁹Ru', '¹⁰⁰Ru', '¹⁰¹Ru', '¹⁰²Ru', '¹⁰³Ru', '¹⁰⁴Ru', '¹⁰⁵Ru', '¹⁰⁶Ru', '¹⁰⁷Ru', '¹⁰⁸Ru', '¹⁰⁹Ru', '¹¹⁰Ru', '¹¹¹Ru', '¹¹²Ru', '¹¹³Ru', '¹¹⁴Ru', '¹¹⁵Ru', '¹¹⁶Ru', '¹¹⁷Ru', '¹¹⁸Ru', '¹¹⁹Ru', '¹²⁰Ru', '⁸⁹Rh', '⁹⁰Rh', '⁹¹Rh', '⁹²Rh', '⁹³Rh', '⁹⁴Rh', '⁹⁵Rh', '⁹⁶Rh', '⁹⁷Rh', '⁹⁸Rh', '⁹⁹Rh', '¹⁰⁰Rh', '¹⁰¹Rh', '¹⁰²Rh', '¹⁰³Rh', '¹⁰⁴Rh', '¹⁰⁵Rh', '¹⁰⁶Rh', '¹⁰⁷Rh', '¹⁰⁸Rh', '¹⁰⁹Rh', '¹¹⁰Rh', '¹¹¹Rh', '¹¹²Rh', '¹¹³Rh', '¹¹⁴Rh', '¹¹⁵Rh', '¹¹⁶Rh', '¹¹⁷Rh', '¹¹⁸Rh', '¹¹⁹Rh', '¹²⁰Rh', '¹²¹Rh', '¹²²Rh', '⁹¹Pd', '⁹²Pd', '⁹³Pd', '⁹⁴Pd', '⁹⁵Pd', '⁹⁶Pd', '⁹⁷Pd', '⁹⁸Pd', '⁹⁹Pd', '¹⁰⁰Pd', '¹⁰¹Pd', '¹⁰²Pd', '¹⁰³Pd', '¹⁰⁴Pd', '¹⁰⁵Pd', '¹⁰⁶Pd', '¹⁰⁷Pd', '¹⁰⁸Pd', '¹⁰⁹Pd', '¹¹⁰Pd', '¹¹¹Pd', '¹¹²Pd', '¹¹³Pd', '¹¹⁴Pd', '¹¹⁵Pd', '¹¹⁶Pd', '¹¹⁷Pd', '¹¹⁸Pd', '¹¹⁹Pd', '¹²⁰Pd', '¹²¹Pd', '¹²²Pd', '¹²³Pd', '¹²⁴Pd', '⁹³Ag', '⁹⁴Ag', '⁹⁵Ag', '⁹⁶Ag', '⁹⁷Ag', '⁹⁸Ag', '⁹⁹Ag', '¹⁰⁰Ag', '¹⁰¹Ag', '¹⁰²Ag', '¹⁰³Ag', '¹⁰⁴Ag', '¹⁰⁵Ag', '¹⁰⁶Ag', '¹⁰⁷Ag', '¹⁰⁸Ag', '¹⁰⁹Ag', '¹¹⁰Ag', '¹¹¹Ag', '¹¹²Ag', '¹¹³Ag', '¹¹⁴Ag', '¹¹⁵Ag', '¹¹⁶Ag', '¹¹⁷Ag', '¹¹⁸Ag', '¹¹⁹Ag', '¹²⁰Ag', '¹²¹Ag', '¹²²Ag', '¹²³Ag', '¹²⁴Ag', '¹²⁵Ag', '¹²⁶Ag', '¹²⁷Ag', '¹²⁸Ag', '¹²⁹Ag', '¹³⁰Ag', '⁹⁵Cd', '⁹⁶Cd', '⁹⁷Cd', '⁹⁸Cd', '⁹⁹Cd', '¹⁰⁰Cd', '¹⁰¹Cd', '¹⁰²Cd', '¹⁰³Cd', '¹⁰⁴Cd', '¹⁰⁵Cd', '¹⁰⁶Cd', '¹⁰⁷Cd', '¹⁰⁸Cd', '¹⁰⁹Cd', '¹¹⁰Cd', '¹¹¹Cd', '¹¹²Cd', '¹¹³Cd', '¹¹⁴Cd', '¹¹⁵Cd', '¹¹⁶Cd', '¹¹⁷Cd', '¹¹⁸Cd', '¹¹⁹Cd', '¹²⁰Cd', '¹²¹Cd', '¹²²Cd', '¹²³Cd', '¹²⁴Cd', '¹²⁵Cd', '¹²⁶Cd', '¹²⁷Cd', '¹²⁸Cd', '¹²⁹Cd', '¹³⁰Cd', '¹³¹Cd', '¹³²Cd', '⁹⁷In', '⁹⁸In', '⁹⁹In', '¹⁰⁰In', '¹⁰¹In', '¹⁰²In', '¹⁰³In', '¹⁰⁴In', '¹⁰⁵In', '¹⁰⁶In', '¹⁰⁷In', '¹⁰⁸In', '¹⁰⁹In', '¹¹⁰In', '¹¹¹In', '¹¹²In', '¹¹³In', '¹¹⁴In', '¹¹⁵In', '¹¹⁶In', '¹¹⁷In', '¹¹⁸In', '¹¹⁹In', '¹²⁰In', '¹²¹In', '¹²²In', '¹²³In', '¹²⁴In', '¹²⁵In', '¹²⁶In', '¹²⁷In', '¹²⁸In', '¹²⁹In', '¹³⁰In', '¹³¹In', '¹³²In', '¹³³In', '¹³⁴In', '¹³⁵In', '⁹⁹Sn', '¹⁰⁰Sn', '¹⁰¹Sn', '¹⁰²Sn', '¹⁰³Sn', '¹⁰⁴Sn', '¹⁰⁵Sn', '¹⁰⁶Sn', '¹⁰⁷Sn', '¹⁰⁸Sn', '¹⁰⁹Sn', '¹¹⁰Sn', '¹¹¹Sn', '¹¹²Sn', '¹¹³Sn', '¹¹⁴Sn', '¹¹⁵Sn', '¹¹⁶Sn', '¹¹⁷Sn', '¹¹⁸Sn', '¹¹⁹Sn', '¹²⁰Sn', '¹²¹Sn', '¹²²Sn', '¹²³Sn', '¹²⁴Sn', '¹²⁵Sn', '¹²⁶Sn', '¹²⁷Sn', '¹²⁸Sn', '¹²⁹Sn', '¹³⁰Sn', '¹³¹Sn', '¹³²Sn', '¹³³Sn', '¹³⁴Sn', '¹³⁵Sn', '¹³⁶Sn', '¹³⁷Sn', '¹⁰³Sb', '¹⁰⁴Sb', '¹⁰⁵Sb', '¹⁰⁶Sb', '¹⁰⁷Sb', '¹⁰⁸Sb', '¹⁰⁹Sb', '¹¹⁰Sb', '¹¹¹Sb', '¹¹²Sb', '¹¹³Sb', '¹¹⁴Sb', '¹¹⁵Sb', '¹¹⁶Sb', '¹¹⁷Sb', '¹¹⁸Sb', '¹¹⁹Sb', '¹²⁰Sb', '¹²¹Sb', '¹²²Sb', '¹²³Sb', '¹²⁴Sb', '¹²⁵Sb', '¹²⁶Sb', '¹²⁷Sb', '¹²⁸Sb', '¹²⁹Sb', '¹³⁰Sb', '¹³¹Sb', '¹³²Sb', '¹³³Sb', '¹³⁴Sb', '¹³⁵Sb', '¹³⁶Sb', '¹³⁷Sb', '¹³⁸Sb', '¹³⁹Sb', '¹⁰⁵Te', '¹⁰⁶Te', '¹⁰⁷Te', '¹⁰⁸Te', '¹⁰⁹Te', '¹¹⁰Te', '¹¹¹Te', '¹¹²Te', '¹¹³Te', '¹¹⁴Te', '¹¹⁵Te', '¹¹⁶Te', '¹¹⁷Te', '¹¹⁸Te', '¹¹⁹Te', '¹²⁰Te', '¹²¹Te', '¹²²Te', '¹²³Te', '¹²⁴Te', '¹²⁵Te', '¹²⁶Te', '¹²⁷Te', '¹²⁸Te', '¹²⁹Te', '¹³⁰Te', '¹³¹Te', '¹³²Te', '¹³³Te', '¹³⁴Te', '¹³⁵Te', '¹³⁶Te', '¹³⁷Te', '¹³⁸Te', '¹³⁹Te', '¹⁴⁰Te', '¹⁴¹Te', '¹⁴²Te', '¹⁰⁸I', '¹⁰⁹I', '¹¹⁰I', '¹¹¹I', '¹¹²I', '¹¹³I', '¹¹⁴I', '¹¹⁵I', '¹¹⁶I', '¹¹⁷I', '¹¹⁸I', '¹¹⁹I', '¹²⁰I', '¹²¹I', '¹²²I', '¹²³I', '¹²⁴I', '¹²⁵I', '¹²⁶I', '¹²⁷I', '¹²⁸I', '¹²⁹I', '¹³⁰I', '¹³¹I', '¹³²I', '¹³³I', '¹³⁴I', '¹³⁵I', '¹³⁶I', '¹³⁷I', '¹³⁸I', '¹³⁹I', '¹⁴⁰I', '¹⁴¹I', '¹⁴²I', '¹⁴³I', '¹⁴⁴I', '¹¹⁰Xe', '¹¹¹Xe', '¹¹²Xe', '¹¹³Xe', '¹¹⁴Xe', '¹¹⁵Xe', '¹¹⁶Xe', '¹¹⁷Xe', '¹¹⁸Xe', '¹¹⁹Xe', '¹²⁰Xe', '¹²¹Xe', '¹²²Xe', '¹²³Xe', '¹²⁴Xe', '¹²⁵Xe', '¹²⁶Xe', '¹²⁷Xe', '¹²⁸Xe', '¹²⁹Xe', '¹³⁰Xe', '¹³¹Xe', '¹³²Xe', '¹³³Xe', '¹³⁴Xe', '¹³⁵Xe', '¹³⁶Xe', '¹³⁷Xe', '¹³⁸Xe', '¹³⁹Xe', '¹⁴⁰Xe', '¹⁴¹Xe', '¹⁴²Xe', '¹⁴³Xe', '¹⁴⁴Xe', '¹⁴⁵Xe', '¹⁴⁶Xe', '¹⁴⁷Xe', '¹¹²Cs', '¹¹³Cs', '¹¹⁴Cs', '¹¹⁵Cs', '¹¹⁶Cs', '¹¹⁷Cs', '¹¹⁸Cs', '¹¹⁹Cs', '¹²⁰Cs', '¹²¹Cs', '¹²²Cs', '¹²³Cs', '¹²⁴Cs', '¹²⁵Cs', '¹²⁶Cs', '¹²⁷Cs', '¹²⁸Cs', '¹²⁹Cs', '¹³⁰Cs', '¹³¹Cs', '¹³²Cs', '¹³³Cs', '¹³⁴Cs', '¹³⁵Cs', '¹³⁶Cs', '¹³⁷Cs', '¹³⁸Cs', '¹³⁹Cs', '¹⁴⁰Cs', '¹⁴¹Cs', '¹⁴²Cs', '¹⁴³Cs', '¹⁴⁴Cs', '¹⁴⁵Cs', '¹⁴⁶Cs', '¹⁴⁷Cs', '¹⁴⁸Cs', '¹⁴⁹Cs', '¹⁵⁰Cs', '¹⁵¹Cs', '¹¹⁴Ba', '¹¹⁵Ba', '¹¹⁶Ba', '¹¹⁷Ba', '¹¹⁸Ba', '¹¹⁹Ba', '¹²⁰Ba', '¹²¹Ba', '¹²²Ba', '¹²³Ba', '¹²⁴Ba', '¹²⁵Ba', '¹²⁶Ba', '¹²⁷Ba', '¹²⁸Ba', '¹²⁹Ba', '¹³⁰Ba', '¹³¹Ba', '¹³²Ba', '¹³³Ba', '¹³⁴Ba', '¹³⁵Ba', '¹³⁶Ba', '¹³⁷Ba', '¹³⁸Ba', '¹³⁹Ba', '¹⁴⁰Ba', '¹⁴¹Ba', '¹⁴²Ba', '¹⁴³Ba', '¹⁴⁴Ba', '¹⁴⁵Ba', '¹⁴⁶Ba', '¹⁴⁷Ba', '¹⁴⁸Ba', '¹⁴⁹Ba', '¹⁵⁰Ba', '¹⁵¹Ba', '¹⁵²Ba', '¹⁵³Ba', '¹¹⁷La', '¹¹⁸La', '¹¹⁹La', '¹²⁰La', '¹²¹La', '¹²²La', '¹²³La', '¹²⁴La', '¹²⁵La', '¹²⁶La', '¹²⁷La', '¹²⁸La', '¹²⁹La', '¹³⁰La', '¹³¹La', '¹³²La', '¹³³La', '¹³⁴La', '¹³⁵La', '¹³⁶La', '¹³⁷La', '¹³⁸La', '¹³⁹La', '¹⁴⁰La', '¹⁴¹La', '¹⁴²La', '¹⁴³La', '¹⁴⁴La', '¹⁴⁵La', '¹⁴⁶La', '¹⁴⁷La', '¹⁴⁸La', '¹⁴⁹La', '¹⁵⁰La', '¹⁵¹La', '¹⁵²La', '¹⁵³La', '¹⁵⁴La', '¹⁵⁵La', '¹¹⁹Ce', '¹²⁰Ce', '¹²¹Ce', '¹²²Ce', '¹²³Ce', '¹²⁴Ce', '¹²⁵Ce', '¹²⁶Ce', '¹²⁷Ce', '¹²⁸Ce', '¹²⁹Ce', '¹³⁰Ce', '¹³¹Ce', '¹³²Ce', '¹³³Ce', '¹³⁴Ce', '¹³⁵Ce', '¹³⁶Ce', '¹³⁷Ce', '¹³⁸Ce', '¹³⁹Ce', '¹⁴⁰Ce', '¹⁴¹Ce', '¹⁴²Ce', '¹⁴³Ce', '¹⁴⁴Ce', '¹⁴⁵Ce', '¹⁴⁶Ce', '¹⁴⁷Ce', '¹⁴⁸Ce', '¹⁴⁹Ce', '¹⁵⁰Ce', '¹⁵¹Ce', '¹⁵²Ce', '¹⁵³Ce', '¹⁵⁴Ce', '¹⁵⁵Ce', '¹⁵⁶Ce', '¹⁵⁷Ce', '¹²¹Pr', '¹²²Pr', '¹²³Pr', '¹²⁴Pr', '¹²⁵Pr', '¹²⁶Pr', '¹²⁷Pr', '¹²⁸Pr', '¹²⁹Pr', '¹³⁰Pr', '¹³¹Pr', '¹³²Pr', '¹³³Pr', '¹³⁴Pr', '¹³⁵Pr', '¹³⁶Pr', '¹³⁷Pr', '¹³⁸Pr', '¹³⁹Pr', '¹⁴⁰Pr', '¹⁴¹Pr', '¹⁴²Pr', '¹⁴³Pr', '¹⁴⁴Pr', '¹⁴⁵Pr', '¹⁴⁶Pr', '¹⁴⁷Pr', '¹⁴⁸Pr', '¹⁴⁹Pr', '¹⁵⁰Pr', '¹⁵¹Pr', '¹⁵²Pr', '¹⁵³Pr', '¹⁵⁴Pr', '¹⁵⁵Pr', '¹⁵⁶Pr', '¹⁵⁷Pr', '¹⁵⁸Pr', '¹⁵⁹Pr', '¹²⁴Nd', '¹²⁵Nd', '¹²⁶Nd', '¹²⁷Nd', '¹²⁸Nd', '¹²⁹Nd', '¹³⁰Nd', '¹³¹Nd', '¹³²Nd', '¹³³Nd', '¹³⁴Nd', '¹³⁵Nd', '¹³⁶Nd', '¹³⁷Nd', '¹³⁸Nd', '¹³⁹Nd', '¹⁴⁰Nd', '¹⁴¹Nd', '¹⁴²Nd', '¹⁴³Nd', '¹⁴⁴Nd', '¹⁴⁵Nd', '¹⁴⁶Nd', '¹⁴⁷Nd', '¹⁴⁸Nd', '¹⁴⁹Nd', '¹⁵⁰Nd', '¹⁵¹Nd', '¹⁵²Nd', '¹⁵³Nd', '¹⁵⁴Nd', '¹⁵⁵Nd', '¹⁵⁶Nd', '¹⁵⁷Nd', '¹⁵⁸Nd', '¹⁵⁹Nd', '¹⁶⁰Nd', '¹⁶¹Nd', '¹²⁶Pm', '¹²⁷Pm', '¹²⁸Pm', '¹²⁹Pm', '¹³⁰Pm', '¹³¹Pm', '¹³²Pm', '¹³³Pm', '¹³⁴Pm', '¹³⁵Pm', '¹³⁶Pm', '¹³⁷Pm', '¹³⁸Pm', '¹³⁹Pm', '¹⁴⁰Pm', '¹⁴¹Pm', '¹⁴²Pm', '¹⁴³Pm', '¹⁴⁴Pm', '¹⁴⁵Pm', '¹⁴⁶Pm', '¹⁴⁷Pm', '¹⁴⁸Pm', '¹⁴⁹Pm', '¹⁵⁰Pm', '¹⁵¹Pm', '¹⁵²Pm', '¹⁵³Pm', '¹⁵⁴Pm', '¹⁵⁵Pm', '¹⁵⁶Pm', '¹⁵⁷Pm', '¹⁵⁸Pm', '¹⁵⁹Pm', '¹⁶⁰Pm', '¹⁶¹Pm', '¹⁶²Pm', '¹⁶³Pm', '¹²⁸Sm', '¹²⁹Sm', '¹³⁰Sm', '¹³¹Sm', '¹³²Sm', '¹³³Sm', '¹³⁴Sm', '¹³⁵Sm', '¹³⁶Sm', '¹³⁷Sm', '¹³⁸Sm', '¹³⁹Sm', '¹⁴⁰Sm', '¹⁴¹Sm', '¹⁴²Sm', '¹⁴³Sm', '¹⁴⁴Sm', '¹⁴⁵Sm', '¹⁴⁶Sm', '¹⁴⁷Sm', '¹⁴⁸Sm', '¹⁴⁹Sm', '¹⁵⁰Sm', '¹⁵¹Sm', '¹⁵²Sm', '¹⁵³Sm', '¹⁵⁴Sm', '¹⁵⁵Sm', '¹⁵⁶Sm', '¹⁵⁷Sm', '¹⁵⁸Sm', '¹⁵⁹Sm', '¹⁶⁰Sm', '¹⁶¹Sm', '¹⁶²Sm', '¹⁶³Sm', '¹⁶⁴Sm', '¹⁶⁵Sm', '¹³⁰Eu', '¹³¹Eu', '¹³²Eu', '¹³³Eu', '¹³⁴Eu', '¹³⁵Eu', '¹³⁶Eu', '¹³⁷Eu', '¹³⁸Eu', '¹³⁹Eu', '¹⁴⁰Eu', '¹⁴¹Eu', '¹⁴²Eu', '¹⁴³Eu', '¹⁴⁴Eu', '¹⁴⁵Eu', '¹⁴⁶Eu', '¹⁴⁷Eu', '¹⁴⁸Eu', '¹⁴⁹Eu', '¹⁵⁰Eu', '¹⁵¹Eu', '¹⁵²Eu', '¹⁵³Eu', '¹⁵⁴Eu', '¹⁵⁵Eu', '¹⁵⁶Eu', '¹⁵⁷Eu', '¹⁵⁸Eu', '¹⁵⁹Eu', '¹⁶⁰Eu', '¹⁶¹Eu', '¹⁶²Eu', '¹⁶³Eu', '¹⁶⁴Eu', '¹⁶⁵Eu', '¹⁶⁶Eu', '¹⁶⁷Eu', '¹³⁴Gd', '¹³⁵Gd', '¹³⁶Gd', '¹³⁷Gd', '¹³⁸Gd', '¹³⁹Gd', '¹⁴⁰Gd', '¹⁴¹Gd', '¹⁴²Gd', '¹⁴³Gd', '¹⁴⁴Gd', '¹⁴⁵Gd', '¹⁴⁶Gd', '¹⁴⁷Gd', '¹⁴⁸Gd', '¹⁴⁹Gd', '¹⁵⁰Gd', '¹⁵¹Gd', '¹⁵²Gd', '¹⁵³Gd', '¹⁵⁴Gd', '¹⁵⁵Gd', '¹⁵⁶Gd', '¹⁵⁷Gd', '¹⁵⁸Gd', '¹⁵⁹Gd', '¹⁶⁰Gd', '¹⁶¹Gd', '¹⁶²Gd', '¹⁶³Gd', '¹⁶⁴Gd', '¹⁶⁵Gd', '¹⁶⁶Gd', '¹⁶⁷Gd', '¹⁶⁸Gd', '¹⁶⁹Gd', '¹³⁶Tb', '¹³⁷Tb', '¹³⁸Tb', '¹³⁹Tb', '¹⁴⁰Tb', '¹⁴¹Tb', '¹⁴²Tb', '¹⁴³Tb', '¹⁴⁴Tb', '¹⁴⁵Tb', '¹⁴⁶Tb', '¹⁴⁷Tb', '¹⁴⁸Tb', '¹⁴⁹Tb', '¹⁵⁰Tb', '¹⁵¹Tb', '¹⁵²Tb', '¹⁵³Tb', '¹⁵⁴Tb', '¹⁵⁵Tb', '¹⁵⁶Tb', '¹⁵⁷Tb', '¹⁵⁸Tb', '¹⁵⁹Tb', '¹⁶⁰Tb', '¹⁶¹Tb', '¹⁶²Tb', '¹⁶³Tb', '¹⁶⁴Tb', '¹⁶⁵Tb', '¹⁶⁶Tb', '¹⁶⁷Tb', '¹⁶⁸Tb', '¹⁶⁹Tb', '¹⁷⁰Tb', '¹⁷¹Tb', '¹³⁸Dy', '¹³⁹Dy', '¹⁴⁰Dy', '¹⁴¹Dy', '¹⁴²Dy', '¹⁴³Dy', '¹⁴⁴Dy', '¹⁴⁵Dy', '¹⁴⁶Dy', '¹⁴⁷Dy', '¹⁴⁸Dy', '¹⁴⁹Dy', '¹⁵⁰Dy', '¹⁵¹Dy', '¹⁵²Dy', '¹⁵³Dy', '¹⁵⁴Dy', '¹⁵⁵Dy', '¹⁵⁶Dy', '¹⁵⁷Dy', '¹⁵⁸Dy', '¹⁵⁹Dy', '¹⁶⁰Dy', '¹⁶¹Dy', '¹⁶²Dy', '¹⁶³Dy', '¹⁶⁴Dy', '¹⁶⁵Dy', '¹⁶⁶Dy', '¹⁶⁷Dy', '¹⁶⁸Dy', '¹⁶⁹Dy', '¹⁷⁰Dy', '¹⁷¹Dy', '¹⁷²Dy', '¹⁷³Dy', '¹⁴⁰Ho', '¹⁴¹Ho', '¹⁴²Ho', '¹⁴³Ho', '¹⁴⁴Ho', '¹⁴⁵Ho', '¹⁴⁶Ho', '¹⁴⁷Ho', '¹⁴⁸Ho', '¹⁴⁹Ho', '¹⁵⁰Ho', '¹⁵¹Ho', '¹⁵²Ho', '¹⁵³Ho', '¹⁵⁴Ho', '¹⁵⁵Ho', '¹⁵⁶Ho', '¹⁵⁷Ho', '¹⁵⁸Ho', '¹⁵⁹Ho', '¹⁶⁰Ho', '¹⁶¹Ho', '¹⁶²Ho', '¹⁶³Ho', '¹⁶⁴Ho', '¹⁶⁵Ho', '¹⁶⁶Ho', '¹⁶⁷Ho', '¹⁶⁸Ho', '¹⁶⁹Ho', '¹⁷⁰Ho', '¹⁷¹Ho', '¹⁷²Ho', '¹⁷³Ho', '¹⁷⁴Ho', '¹⁷⁵Ho', '¹⁴³Er', '¹⁴⁴Er', '¹⁴⁵Er', '¹⁴⁶Er', '¹⁴⁷Er', '¹⁴⁸Er', '¹⁴⁹Er', '¹⁵⁰Er', '¹⁵¹Er', '¹⁵²Er', '¹⁵³Er', '¹⁵⁴Er', '¹⁵⁵Er', '¹⁵⁶Er', '¹⁵⁷Er', '¹⁵⁸Er', '¹⁵⁹Er', '¹⁶⁰Er', '¹⁶¹Er', '¹⁶²Er', '¹⁶³Er', '¹⁶⁴Er', '¹⁶⁵Er', '¹⁶⁶Er', '¹⁶⁷Er', '¹⁶⁸Er', '¹⁶⁹Er', '¹⁷⁰Er', '¹⁷¹Er', '¹⁷²Er', '¹⁷³Er', '¹⁷⁴Er', '¹⁷⁵Er', '¹⁷⁶Er', '¹⁷⁷Er', '¹⁴⁵Tm', '¹⁴⁶Tm', '¹⁴⁷Tm', '¹⁴⁸Tm', '¹⁴⁹Tm', '¹⁵⁰Tm', '¹⁵¹Tm', '¹⁵²Tm', '¹⁵³Tm', '¹⁵⁴Tm', '¹⁵⁵Tm', '¹⁵⁶Tm', '¹⁵⁷Tm', '¹⁵⁸Tm', '¹⁵⁹Tm', '¹⁶⁰Tm', '¹⁶¹Tm', '¹⁶²Tm', '¹⁶³Tm', '¹⁶⁴Tm', '¹⁶⁵Tm', '¹⁶⁶Tm', '¹⁶⁷Tm', '¹⁶⁸Tm', '¹⁶⁹Tm', '¹⁷⁰Tm', '¹⁷¹Tm', '¹⁷²Tm', '¹⁷³Tm', '¹⁷⁴Tm', '¹⁷⁵Tm', '¹⁷⁶Tm', '¹⁷⁷Tm', '¹⁷⁸Tm', '¹⁷⁹Tm', '¹⁴⁸Yb', '¹⁴⁹Yb', '¹⁵⁰Yb', '¹⁵¹Yb', '¹⁵²Yb', '¹⁵³Yb', '¹⁵⁴Yb', '¹⁵⁵Yb', '¹⁵⁶Yb', '¹⁵⁷Yb', '¹⁵⁸Yb', '¹⁵⁹Yb', '¹⁶⁰Yb', '¹⁶¹Yb', '¹⁶²Yb', '¹⁶³Yb', '¹⁶⁴Yb', '¹⁶⁵Yb', '¹⁶⁶Yb', '¹⁶⁷Yb', '¹⁶⁸Yb', '¹⁶⁹Yb', '¹⁷⁰Yb', '¹⁷¹Yb', '¹⁷²Yb', '¹⁷³Yb', '¹⁷⁴Yb', '¹⁷⁵Yb', '¹⁷⁶Yb', '¹⁷⁷Yb', '¹⁷⁸Yb', '¹⁷⁹Yb', '¹⁸⁰Yb', '¹⁸¹Yb', '¹⁸²Yb', '¹⁵⁰Lu', '¹⁵¹Lu', '¹⁵²Lu', '¹⁵³Lu', '¹⁵⁴Lu', '¹⁵⁵Lu', '¹⁵⁶Lu', '¹⁵⁷Lu', '¹⁵⁸Lu', '¹⁵⁹Lu', '¹⁶⁰Lu', '¹⁶¹Lu', '¹⁶²Lu', '¹⁶³Lu', '¹⁶⁴Lu', '¹⁶⁵Lu', '¹⁶⁶Lu', '¹⁶⁷Lu', '¹⁶⁸Lu', '¹⁶⁹Lu', '¹⁷⁰Lu', '¹⁷¹Lu', '¹⁷²Lu', '¹⁷³Lu', '¹⁷⁴Lu', '¹⁷⁵Lu', '¹⁷⁶Lu', '¹⁷⁷Lu', '¹⁷⁸Lu', '¹⁷⁹Lu', '¹⁸⁰Lu', '¹⁸¹Lu', '¹⁸²Lu', '¹⁸³Lu', '¹⁸⁴Lu', '¹⁵³Hf', '¹⁵⁴Hf', '¹⁵⁵Hf', '¹⁵⁶Hf', '¹⁵⁷Hf', '¹⁵⁸Hf', '¹⁵⁹Hf', '¹⁶⁰Hf', '¹⁶¹Hf', '¹⁶²Hf', '¹⁶³Hf', '¹⁶⁴Hf', '¹⁶⁵Hf', '¹⁶⁶Hf', '¹⁶⁷Hf', '¹⁶⁸Hf', '¹⁶⁹Hf', '¹⁷⁰Hf', '¹⁷¹Hf', '¹⁷²Hf', '¹⁷³Hf', '¹⁷⁴Hf', '¹⁷⁵Hf', '¹⁷⁶Hf', '¹⁷⁷Hf', '¹⁷⁸Hf', '¹⁷⁹Hf', '¹⁸⁰Hf', '¹⁸¹Hf', '¹⁸²Hf', '¹⁸³Hf', '¹⁸⁴Hf', '¹⁸⁵Hf', '¹⁸⁶Hf', '¹⁸⁷Hf', '¹⁸⁸Hf', '¹⁵⁵Ta', '¹⁵⁶Ta', '¹⁵⁷Ta', '¹⁵⁸Ta', '¹⁵⁹Ta', '¹⁶⁰Ta', '¹⁶¹Ta', '¹⁶²Ta', '¹⁶³Ta', '¹⁶⁴Ta', '¹⁶⁵Ta', '¹⁶⁶Ta', '¹⁶⁷Ta', '¹⁶⁸Ta', '¹⁶⁹Ta', '¹⁷⁰Ta', '¹⁷¹Ta', '¹⁷²Ta', '¹⁷³Ta', '¹⁷⁴Ta', '¹⁷⁵Ta', '¹⁷⁶Ta', '¹⁷⁷Ta', '¹⁷⁸Ta', '¹⁷⁹Ta', '¹⁸⁰Ta', '¹⁸¹Ta', '¹⁸²Ta', '¹⁸³Ta', '¹⁸⁴Ta', '¹⁸⁵Ta', '¹⁸⁶Ta', '¹⁸⁷Ta', '¹⁸⁸Ta', '¹⁸⁹Ta', '¹⁹⁰Ta', '¹⁵⁸W', '¹⁵⁹W', '¹⁶⁰W', '¹⁶¹W', '¹⁶²W', '¹⁶³W', '¹⁶⁴W', '¹⁶⁵W', '¹⁶⁶W', '¹⁶⁷W', '¹⁶⁸W', '¹⁶⁹W', '¹⁷⁰W', '¹⁷¹W', '¹⁷²W', '¹⁷³W', '¹⁷⁴W', '¹⁷⁵W', '¹⁷⁶W', '¹⁷⁷W', '¹⁷⁸W', '¹⁷⁹W', '¹⁸⁰W', '¹⁸¹W', '¹⁸²W', '¹⁸³W', '¹⁸⁴W', '¹⁸⁵W', '¹⁸⁶W', '¹⁸⁷W', '¹⁸⁸W', '¹⁸⁹W', '¹⁹⁰W', '¹⁹¹W', '¹⁹²W', '¹⁶⁰Re', '¹⁶¹Re', '¹⁶²Re', '¹⁶³Re', '¹⁶⁴Re', '¹⁶⁵Re', '¹⁶⁶Re', '¹⁶⁷Re', '¹⁶⁸Re', '¹⁶⁹Re', '¹⁷⁰Re', '¹⁷¹Re', '¹⁷²Re', '¹⁷³Re', '¹⁷⁴Re', '¹⁷⁵Re', '¹⁷⁶Re', '¹⁷⁷Re', '¹⁷⁸Re', '¹⁷⁹Re', '¹⁸⁰Re', '¹⁸¹Re', '¹⁸²Re', '¹⁸³Re', '¹⁸⁴Re', '¹⁸⁵Re', '¹⁸⁶Re', '¹⁸⁷Re', '¹⁸⁸Re', '¹⁸⁹Re', '¹⁹⁰Re', '¹⁹¹Re', '¹⁹²Re', '¹⁹³Re', '¹⁹⁴Re', '¹⁶²Os', '¹⁶³Os', '¹⁶⁴Os', '¹⁶⁵Os', '¹⁶⁶Os', '¹⁶⁷Os', '¹⁶⁸Os', '¹⁶⁹Os', '¹⁷⁰Os', '¹⁷¹Os', '¹⁷²Os', '¹⁷³Os', '¹⁷⁴Os', '¹⁷⁵Os', '¹⁷⁶Os', '¹⁷⁷Os', '¹⁷⁸Os', '¹⁷⁹Os', '¹⁸⁰Os', '¹⁸¹Os', '¹⁸²Os', '¹⁸³Os', '¹⁸⁴Os', '¹⁸⁵Os', '¹⁸⁶Os', '¹⁸⁷Os', '¹⁸⁸Os', '¹⁸⁹Os', '¹⁹⁰Os', '¹⁹¹Os', '¹⁹²Os', '¹⁹³Os', '¹⁹⁴Os', '¹⁹⁵Os', '¹⁹⁶Os', '¹⁶⁴Ir', '¹⁶⁵Ir', '¹⁶⁶Ir', '¹⁶⁷Ir', '¹⁶⁸Ir', '¹⁶⁹Ir', '¹⁷⁰Ir', '¹⁷¹Ir', '¹⁷²Ir', '¹⁷³Ir', '¹⁷⁴Ir', '¹⁷⁵Ir', '¹⁷⁶Ir', '¹⁷⁷Ir', '¹⁷⁸Ir', '¹⁷⁹Ir', '¹⁸⁰Ir', '¹⁸¹Ir', '¹⁸²Ir', '¹⁸³Ir', '¹⁸⁴Ir', '¹⁸⁵Ir', '¹⁸⁶Ir', '¹⁸⁷Ir', '¹⁸⁸Ir', '¹⁸⁹Ir', '¹⁹⁰Ir', '¹⁹¹Ir', '¹⁹²Ir', '¹⁹³Ir', '¹⁹⁴Ir', '¹⁹⁵Ir', '¹⁹⁶Ir', '¹⁹⁷Ir', '¹⁹⁸Ir', '¹⁹⁹Ir', '¹⁶⁶Pt', '¹⁶⁷Pt', '¹⁶⁸Pt', '¹⁶⁹Pt', '¹⁷⁰Pt', '¹⁷¹Pt', '¹⁷²Pt', '¹⁷³Pt', '¹⁷⁴Pt', '¹⁷⁵Pt', '¹⁷⁶Pt', '¹⁷⁷Pt', '¹⁷⁸Pt', '¹⁷⁹Pt', '¹⁸⁰Pt', '¹⁸¹Pt', '¹⁸²Pt', '¹⁸³Pt', '¹⁸⁴Pt', '¹⁸⁵Pt', '¹⁸⁶Pt', '¹⁸⁷Pt', '¹⁸⁸Pt', '¹⁸⁹Pt', '¹⁹⁰Pt', '¹⁹¹Pt', '¹⁹²Pt', '¹⁹³Pt', '¹⁹⁴Pt', '¹⁹⁵Pt', '¹⁹⁶Pt', '¹⁹⁷Pt', '¹⁹⁸Pt', '¹⁹⁹Pt', '²⁰⁰Pt', '²⁰¹Pt', '²⁰²Pt', '¹⁶⁹Au', '¹⁷⁰Au', '¹⁷¹Au', '¹⁷²Au', '¹⁷³Au', '¹⁷⁴Au', '¹⁷⁵Au', '¹⁷⁶Au', '¹⁷⁷Au', '¹⁷⁸Au', '¹⁷⁹Au', '¹⁸⁰Au', '¹⁸¹Au', '¹⁸²Au', '¹⁸³Au', '¹⁸⁴Au', '¹⁸⁵Au', '¹⁸⁶Au', '¹⁸⁷Au', '¹⁸⁸Au', '¹⁸⁹Au', '¹⁹⁰Au', '¹⁹¹Au', '¹⁹²Au', '¹⁹³Au', '¹⁹⁴Au', '¹⁹⁵Au', '¹⁹⁶Au', '¹⁹⁷Au', '¹⁹⁸Au', '¹⁹⁹Au', '²⁰⁰Au', '²⁰¹Au', '²⁰²Au', '²⁰³Au', '²⁰⁴Au', '²⁰⁵Au', '¹⁷¹Hg', '¹⁷²Hg', '¹⁷³Hg', '¹⁷⁴Hg', '¹⁷⁵Hg', '¹⁷⁶Hg', '¹⁷⁷Hg', '¹⁷⁸Hg', '¹⁷⁹Hg', '¹⁸⁰Hg', '¹⁸¹Hg', '¹⁸²Hg', '¹⁸³Hg', '¹⁸⁴Hg', '¹⁸⁵Hg', '¹⁸⁶Hg', '¹⁸⁷Hg', '¹⁸⁸Hg', '¹⁸⁹Hg', '¹⁹⁰Hg', '¹⁹¹Hg', '¹⁹²Hg', '¹⁹³Hg', '¹⁹⁴Hg', '¹⁹⁵Hg', '¹⁹⁶Hg', '¹⁹⁷Hg', '¹⁹⁸Hg', '¹⁹⁹Hg', '²⁰⁰Hg', '²⁰¹Hg', '²⁰²Hg', '²⁰³Hg', '²⁰⁴Hg', '²⁰⁵Hg', '²⁰⁶Hg', '²⁰⁷Hg', '²⁰⁸Hg', '²⁰⁹Hg', '²¹⁰Hg', '¹⁷⁶Tl', '¹⁷⁷Tl', '¹⁷⁸Tl', '¹⁷⁹Tl', '¹⁸⁰Tl', '¹⁸¹Tl', '¹⁸²Tl', '¹⁸³Tl', '¹⁸⁴Tl', '¹⁸⁵Tl', '¹⁸⁶Tl', '¹⁸⁷Tl', '¹⁸⁸Tl', '¹⁸⁹Tl', '¹⁹⁰Tl', '¹⁹¹Tl', '¹⁹²Tl', '¹⁹³Tl', '¹⁹⁴Tl', '¹⁹⁵Tl', '¹⁹⁶Tl', '¹⁹⁷Tl', '¹⁹⁸Tl', '¹⁹⁹Tl', '²⁰⁰Tl', '²⁰¹Tl', '²⁰²Tl', '²⁰³Tl', '²⁰⁴Tl', '²⁰⁵Tl', '²⁰⁶Tl', '²⁰⁷Tl', '²⁰⁸Tl', '²⁰⁹Tl', '²¹⁰Tl', '²¹¹Tl', '²¹²Tl', '¹⁷⁸Pb', '¹⁷⁹Pb', '¹⁸⁰Pb', '¹⁸¹Pb', '¹⁸²Pb', '¹⁸³Pb', '¹⁸⁴Pb', '¹⁸⁵Pb', '¹⁸⁶Pb', '¹⁸⁷Pb', '¹⁸⁸Pb', '¹⁸⁹Pb', '¹⁹⁰Pb', '¹⁹¹Pb', '¹⁹²Pb', '¹⁹³Pb', '¹⁹⁴Pb', '¹⁹⁵Pb', '¹⁹⁶Pb', '¹⁹⁷Pb', '¹⁹⁸Pb', '¹⁹⁹Pb', '²⁰⁰Pb', '²⁰¹Pb', '²⁰²Pb', '²⁰³Pb', '²⁰⁴Pb', '²⁰⁵Pb', '²⁰⁶Pb', '²⁰⁷Pb', '²⁰⁸Pb', '²⁰⁹Pb', '²¹⁰Pb', '²¹¹Pb', '²¹²Pb', '²¹³Pb', '²¹⁴Pb', '²¹⁵Pb', '¹⁸⁴Bi', '¹⁸⁵Bi', '¹⁸⁶Bi', '¹⁸⁷Bi', '¹⁸⁸Bi', '¹⁸⁹Bi', '¹⁹⁰Bi', '¹⁹¹Bi', '¹⁹²Bi', '¹⁹³Bi', '¹⁹⁴Bi', '¹⁹⁵Bi', '¹⁹⁶Bi', '¹⁹⁷Bi', '¹⁹⁸Bi', '¹⁹⁹Bi', '²⁰⁰Bi', '²⁰¹Bi', '²⁰²Bi', '²⁰³Bi', '²⁰⁴Bi', '²⁰⁵Bi', '²⁰⁶Bi', '²⁰⁷Bi', '²⁰⁸Bi', '²⁰⁹Bi', '²¹⁰Bi', '²¹¹Bi', '²¹²Bi', '²¹³Bi', '²¹⁴Bi', '²¹⁵Bi', '²¹⁶Bi', '²¹⁷Bi', '²¹⁸Bi', '²¹⁹Bi', '¹⁸⁸Po', '¹⁸⁹Po', '¹⁹⁰Po', '¹⁹¹Po', '¹⁹²Po', '¹⁹³Po', '¹⁹⁴Po', '¹⁹⁵Po', '¹⁹⁶Po', '¹⁹⁷Po', '¹⁹⁸Po', '¹⁹⁹Po', '²⁰⁰Po', '²⁰¹Po', '²⁰²Po', '²⁰³Po', '²⁰⁴Po', '²⁰⁵Po', '²⁰⁶Po', '²⁰⁷Po', '²⁰⁸Po', '²⁰⁹Po', '²¹⁰Po', '²¹¹Po', '²¹²Po', '²¹³Po', '²¹⁴Po', '²¹⁵Po', '²¹⁶Po', '²¹⁷Po', '²¹⁸Po', '²¹⁹Po', '²²⁰Po', '¹⁹³At', '¹⁹⁴At', '¹⁹⁵At', '¹⁹⁶At', '¹⁹⁷At', '¹⁹⁸At', '¹⁹⁹At', '²⁰⁰At', '²⁰¹At', '²⁰²At', '²⁰³At', '²⁰⁴At', '²⁰⁵At', '²⁰⁶At', '²⁰⁷At', '²⁰⁸At', '²⁰⁹At', '²¹⁰At', '²¹¹At', '²¹²At', '²¹³At', '²¹⁴At', '²¹⁵At', '²¹⁶At', '²¹⁷At', '²¹⁸At', '²¹⁹At', '²²⁰At', '²²¹At', '²²²At', '²²³At', '¹⁹⁵Rn', '¹⁹⁶Rn', '¹⁹⁷Rn', '¹⁹⁸Rn', '¹⁹⁹Rn', '²⁰⁰Rn', '²⁰¹Rn', '²⁰²Rn', '²⁰³Rn', '²⁰⁴Rn', '²⁰⁵Rn', '²⁰⁶Rn', '²⁰⁷Rn', '²⁰⁸Rn', '²⁰⁹Rn', '²¹⁰Rn', '²¹¹Rn', '²¹²Rn', '²¹³Rn', '²¹⁴Rn', '²¹⁵Rn', '²¹⁶Rn', '²¹⁷Rn', '²¹⁸Rn', '²¹⁹Rn', '²²⁰Rn', '²²¹Rn', '²²²Rn', '²²³Rn', '²²⁴Rn', '²²⁵Rn', '²²⁶Rn', '²²⁷Rn', '²²⁸Rn', '¹⁹⁹Fr', '²⁰⁰Fr', '²⁰¹Fr', '²⁰²Fr', '²⁰³Fr', '²⁰⁴Fr', '²⁰⁵Fr', '²⁰⁶Fr', '²⁰⁷Fr', '²⁰⁸Fr', '²⁰⁹Fr', '²¹⁰Fr', '²¹¹Fr', '²¹²Fr', '²¹³Fr', '²¹⁴Fr', '²¹⁵Fr', '²¹⁶Fr', '²¹⁷Fr', '²¹⁸Fr', '²¹⁹Fr', '²²⁰Fr', '²²¹Fr', '²²²Fr', '²²³Fr', '²²⁴Fr', '²²⁵Fr', '²²⁶Fr', '²²⁷Fr', '²²⁸Fr', '²²⁹Fr', '²³⁰Fr', '²³¹Fr', '²³²Fr', '²⁰²Ra', '²⁰³Ra', '²⁰⁴Ra', '²⁰⁵Ra', '²⁰⁶Ra', '²⁰⁷Ra', '²⁰⁸Ra', '²⁰⁹Ra', '²¹⁰Ra', '²¹¹Ra', '²¹²Ra', '²¹³Ra', '²¹⁴Ra', '²¹⁵Ra', '²¹⁶Ra', '²¹⁷Ra', '²¹⁸Ra', '²¹⁹Ra', '²²⁰Ra', '²²¹Ra', '²²²Ra', '²²³Ra', '²²⁴Ra', '²²⁵Ra', '²²⁶Ra', '²²⁷Ra', '²²⁸Ra', '²²⁹Ra', '²³⁰Ra', '²³¹Ra', '²³²Ra', '²³³Ra', '²³⁴Ra', '²⁰⁶Ac', '²⁰⁷Ac', '²⁰⁸Ac', '²⁰⁹Ac', '²¹⁰Ac', '²¹¹Ac', '²¹²Ac', '²¹³Ac', '²¹⁴Ac', '²¹⁵Ac', '²¹⁶Ac', '²¹⁷Ac', '²¹⁸Ac', '²¹⁹Ac', '²²⁰Ac', '²²¹Ac', '²²²Ac', '²²³Ac', '²²⁴Ac', '²²⁵Ac', '²²⁶Ac', '²²⁷Ac', '²²⁸Ac', '²²⁹Ac', '²³⁰Ac', '²³¹Ac', '²³²Ac', '²³³Ac', '²³⁴Ac', '²³⁵Ac', '²³⁶Ac', '²⁰⁹Th', '²¹⁰Th', '²¹¹Th', '²¹²Th', '²¹³Th', '²¹⁴Th', '²¹⁵Th', '²¹⁶Th', '²¹⁷Th', '²¹⁸Th', '²¹⁹Th', '²²⁰Th', '²²¹Th', '²²²Th', '²²³Th', '²²⁴Th', '²²⁵Th', '²²⁶Th', '²²⁷Th', '²²⁸Th', '²²⁹Th', '²³⁰Th', '²³¹Th', '²³²Th', '²³³Th', '²³⁴Th', '²³⁵Th', '²³⁶Th', '²³⁷Th', '²³⁸Th', '²¹²Pa', '²¹³Pa', '²¹⁴Pa', '²¹⁵Pa', '²¹⁶Pa', '²¹⁷Pa', '²¹⁸Pa', '²¹⁹Pa', '²²⁰Pa', '²²¹Pa', '²²²Pa', '²²³Pa', '²²⁴Pa', '²²⁵Pa', '²²⁶Pa', '²²⁷Pa', '²²⁸Pa', '²²⁹Pa', '²³⁰Pa', '²³¹Pa', '²³²Pa', '²³³Pa', '²³⁴Pa', '²³⁵Pa', '²³⁶Pa', '²³⁷Pa', '²³⁸Pa', '²³⁹Pa', '²⁴⁰Pa', '²¹⁷U', '²¹⁸U', '²¹⁹U', '²²⁰U', '²²¹U', '²²²U', '²²³U', '²²⁴U', '²²⁵U', '²²⁶U', '²²⁷U', '²²⁸U', '²²⁹U', '²³⁰U', '²³¹U', '²³²U', '²³³U', '²³⁴U', '²³⁵U', '²³⁶U', '²³⁷U', '²³⁸U', '²³⁹U', '²⁴⁰U', '²⁴¹U', '²⁴²U', '²²⁵Np', '²²⁶Np', '²²⁷Np', '²²⁸Np', '²²⁹Np', '²³⁰Np', '²³¹Np', '²³²Np', '²³³Np', '²³⁴Np', '²³⁵Np', '²³⁶Np', '²³⁷Np', '²³⁸Np', '²³⁹Np', '²⁴⁰Np', '²⁴¹Np', '²⁴²Np', '²⁴³Np', '²⁴⁴Np', '²²⁸Pu', '²²⁹Pu', '²³⁰Pu', '²³¹Pu', '²³²Pu', '²³³Pu', '²³⁴Pu', '²³⁵Pu', '²³⁶Pu', '²³⁷Pu', '²³⁸Pu', '²³⁹Pu', '²⁴⁰Pu', '²⁴¹Pu', '²⁴²Pu', '²⁴³Pu', '²⁴⁴Pu', '²⁴⁵Pu', '²⁴⁶Pu', '²⁴⁷Pu', '²³¹Am', '²³²Am', '²³³Am', '²³⁴Am', '²³⁵Am', '²³⁶Am', '²³⁷Am', '²³⁸Am', '²³⁹Am', '²⁴⁰Am', '²⁴¹Am', '²⁴²Am', '²⁴³Am', '²⁴⁴Am', '²⁴⁵Am', '²⁴⁶Am', '²⁴⁷Am', '²⁴⁸Am', '²⁴⁹Am', '²³³Cm', '²³⁴Cm', '²³⁵Cm', '²³⁶Cm', '²³⁷Cm', '²³⁸Cm', '²³⁹Cm', '²⁴⁰Cm', '²⁴¹Cm', '²⁴²Cm', '²⁴³Cm', '²⁴⁴Cm', '²⁴⁵Cm', '²⁴⁶Cm', '²⁴⁷Cm', '²⁴⁸Cm', '²⁴⁹Cm', '²⁵⁰Cm', '²⁵¹Cm', '²⁵²Cm', '²³⁵Bk', '²³⁶Bk', '²³⁷Bk', '²³⁸Bk', '²³⁹Bk', '²⁴⁰Bk', '²⁴¹Bk', '²⁴²Bk', '²⁴³Bk', '²⁴⁴Bk', '²⁴⁵Bk', '²⁴⁶Bk', '²⁴⁷Bk', '²⁴⁸Bk', '²⁴⁹Bk', '²⁵⁰Bk', '²⁵¹Bk', '²⁵²Bk', '²⁵³Bk', '²⁵⁴Bk', '²³⁷Cf', '²³⁸Cf', '²³⁹Cf', '²⁴⁰Cf', '²⁴¹Cf', '²⁴²Cf', '²⁴³Cf', '²⁴⁴Cf', '²⁴⁵Cf', '²⁴⁶Cf', '²⁴⁷Cf', '²⁴⁸Cf', '²⁴⁹Cf', '²⁵⁰Cf', '²⁵¹Cf', '²⁵²Cf', '²⁵³Cf', '²⁵⁴Cf', '²⁵⁵Cf', '²⁵⁶Cf', '²⁴⁰Es', '²⁴¹Es', '²⁴²Es', '²⁴³Es', '²⁴⁴Es', '²⁴⁵Es', '²⁴⁶Es', '²⁴⁷Es', '²⁴⁸Es', '²⁴⁹Es', '²⁵⁰Es', '²⁵¹Es', '²⁵²Es', '²⁵³Es', '²⁵⁴Es', '²⁵⁵Es', '²⁵⁶Es', '²⁵⁷Es', '²⁵⁸Es', '²⁴²Fm', '²⁴³Fm', '²⁴⁴Fm', '²⁴⁵Fm', '²⁴⁶Fm', '²⁴⁷Fm', '²⁴⁸Fm', '²⁴⁹Fm', '²⁵⁰Fm', '²⁵¹Fm', '²⁵²Fm', '²⁵³Fm', '²⁵⁴Fm', '²⁵⁵Fm', '²⁵⁶Fm', '²⁵⁷Fm', '²⁵⁸Fm', '²⁵⁹Fm', '²⁶⁰Fm', '²⁴⁵Md', '²⁴⁶Md', '²⁴⁷Md', '²⁴⁸Md', '²⁴⁹Md', '²⁵⁰Md', '²⁵¹Md', '²⁵²Md', '²⁵³Md', '²⁵⁴Md', '²⁵⁵Md', '²⁵⁶Md', '²⁵⁷Md', '²⁵⁸Md', '²⁵⁹Md', '²⁶⁰Md', '²⁶¹Md', '²⁶²Md', '²⁴⁸No', '²⁴⁹No', '²⁵⁰No', '²⁵¹No', '²⁵²No', '²⁵³No', '²⁵⁴No', '²⁵⁵No', '²⁵⁶No', '²⁵⁷No', '²⁵⁸No', '²⁵⁹No', '²⁶⁰No', '²⁶¹No', '²⁶²No', '²⁶³No', '²⁶⁴No', '²⁵¹Lr', '²⁵²Lr', '²⁵³Lr', '²⁵⁴Lr', '²⁵⁵Lr', '²⁵⁶Lr', '²⁵⁷Lr', '²⁵⁸Lr', '²⁵⁹Lr', '²⁶⁰Lr', '²⁶¹Lr', '²⁶²Lr', '²⁶³Lr', '²⁶⁴Lr', '²⁶⁵Lr', '²⁶⁶Lr', '²⁵³Rf', '²⁵⁴Rf', '²⁵⁵Rf', '²⁵⁶Rf', '²⁵⁷Rf', '²⁵⁸Rf', '²⁵⁹Rf', '²⁶⁰Rf', '²⁶¹Rf', '²⁶²Rf', '²⁶³Rf', '²⁶⁴Rf', '²⁶⁵Rf', '²⁶⁶Rf', '²⁶⁷Rf', '²⁶⁸Rf', '²⁵⁵Db', '²⁵⁶Db', '²⁵⁷Db', '²⁵⁸Db', '²⁵⁹Db', '²⁶⁰Db', '²⁶¹Db', '²⁶²Db', '²⁶³Db', '²⁶⁴Db', '²⁶⁵Db', '²⁶⁶Db', '²⁶⁷Db', '²⁶⁸Db', '²⁶⁹Db', '²⁷⁰Db', '²⁵⁸Sg', '²⁵⁹Sg', '²⁶⁰Sg', '²⁶¹Sg', '²⁶²Sg', '²⁶³Sg', '²⁶⁴Sg', '²⁶⁵Sg', '²⁶⁶Sg', '²⁶⁷Sg', '²⁶⁸Sg', '²⁶⁹Sg', '²⁷⁰Sg', '²⁷¹Sg', '²⁷²Sg', '²⁷³Sg', '²⁶⁰Bh', '²⁶¹Bh', '²⁶²Bh', '²⁶³Bh', '²⁶⁴Bh', '²⁶⁵Bh', '²⁶⁶Bh', '²⁶⁷Bh', '²⁶⁸Bh', '²⁶⁹Bh', '²⁷⁰Bh', '²⁷¹Bh', '²⁷²Bh', '²⁷³Bh', '²⁷⁴Bh', '²⁷⁵Bh', '²⁶³Hs', '²⁶⁴Hs', '²⁶⁵Hs', '²⁶⁶Hs', '²⁶⁷Hs', '²⁶⁸Hs', '²⁶⁹Hs', '²⁷⁰Hs', '²⁷¹Hs', '²⁷²Hs', '²⁷³Hs', '²⁷⁴Hs', '²⁷⁵Hs', '²⁷⁶Hs', '²⁷⁷Hs', '²⁶⁵Mt', '²⁶⁶Mt', '²⁶⁷Mt', '²⁶⁸Mt', '²⁶⁹Mt', '²⁷⁰Mt', '²⁷¹Mt', '²⁷²Mt', '²⁷³Mt', '²⁷⁴Mt', '²⁷⁵Mt', '²⁷⁶Mt', '²⁷⁷Mt', '²⁷⁸Mt', '²⁷⁹Mt', '²⁶⁷Ds', '²⁶⁸Ds', '²⁶⁹Ds', '²⁷⁰Ds', '²⁷¹Ds', '²⁷²Ds', '²⁷³Ds', '²⁷⁴Ds', '²⁷⁵Ds', '²⁷⁶Ds', '²⁷⁷Ds', '²⁷⁸Ds', '²⁷⁹Ds', '²⁸⁰Ds', '²⁸¹Ds', '²⁷²Rg', '²⁷³Rg', '²⁷⁴Rg', '²⁷⁵Rg', '²⁷⁶Rg', '²⁷⁷Rg', '²⁷⁸Rg', '²⁷⁹Rg', '²⁸⁰Rg', '²⁸¹Rg', '²⁸²Rg', '²⁸³Rg', '²⁷⁷Cn', '²⁷⁸Cn', '²⁷⁹Cn', '²⁸⁰Cn', '²⁸¹Cn', '²⁸²Cn', '²⁸³Cn', '²⁸⁴Cn', '²⁸⁵Cn', '²⁸³Nh', '²⁸⁴Nh', '²⁸⁵Nh', '²⁸⁶Nh', '²⁸⁷Nh', '²⁸⁵Fl', '²⁸⁶Fl', '²⁸⁷Fl', '²⁸⁸Fl', '²⁸⁹Fl', '²⁸⁷Mc', '²⁸⁸Mc', '²⁸⁹Mc', '²⁹⁰Mc', '²⁹¹Mc', '²⁸⁹Lv', '²⁹⁰Lv', '²⁹¹Lv', '²⁹²Lv', '²⁹¹Ts', '²⁹²Ts', '²⁹³Ts', '²⁹⁴Ts', '²⁹³Og']
#"₀₁₂₃₄₅₆₇₈₉₊₋"

elements = [
    "H",  "He", "Li", "Be", "B",  "C",  "N",  "O",  "F",  "Ne",
    "Na", "Mg", "Al", "Si", "P",  "S",  "Cl", "Ar", "K",  "Ca",
    "Sc", "Ti", "V",  "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y",  "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I",  "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W",  "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U",  "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]
nuclides += elements
emission_lines = ['Kα₁','Kα₂','Kβ₁','Lα₁','Lα₂','Lβ₂','Lα₁','Lγ₁','Mα₁']

for n in nuclides:
    for e in emission_lines:
        length_bases.append(f'xu({n} {e})')
for S in Si_units:
    for l in length_bases:
        length_units.append(f'{S}{l}')

print('done')

length_units_lists = list(batched(length_units,len(length_units)//120))
print(len(length_units_lists[0]))
CHAR_GROUPS = [

    
    
]

for i in length_units_lists:
    CHAR_GROUPS.append((f'length units {length_units_lists.index(i)}',i))



COLS = 8

BG        = "#0f0f13"
PANEL     = "#17171f"
ACCENT    = "#6c63ff"
BTN_BG    = "#1e1e2e"
BTN_FG    = "#e0e0f5"
BTN_HOV   = "#2e2e45"
TAB_ACT   = "#6c63ff"
TAB_INACT = "#1e1e2e"
TOAST_BG  = "#6c63ff"
LABEL_FG  = "#888899"
SB_TROUGH = "#17171f"
SB_THUMB  = "#3a3a55"


class ScrollableTabBar(tk.Frame):
    """A horizontally scrollable row of tab buttons."""

    def __init__(self, parent, tab_names, on_select, tab_f, **kwargs):
        super().__init__(parent, bg=BG, **kwargs)

        self._canvas = tk.Canvas(self, bg=BG, height=38,
                                 highlightthickness=0, bd=0)
        self._sb = tk.Scrollbar(self, orient="horizontal",
                                command=self._canvas.xview,
                                troughcolor=SB_TROUGH,
                                bg=SB_THUMB, activebackground=ACCENT,
                                highlightthickness=0, bd=0)
        self._canvas.configure(xscrollcommand=self._sb.set)
        self._canvas.pack(side="top", fill="x", expand=True)
        self._sb.pack(side="bottom", fill="x")

        self._inner = tk.Frame(self._canvas, bg=BG)
        self._win_id = self._canvas.create_window((0, 0), window=self._inner, anchor="nw")

        self._inner.bind("<Configure>", self._on_inner_configure)
        self._canvas.bind("<Configure>", self._on_canvas_configure)
        self._canvas.bind("<MouseWheel>", self._on_mousewheel)
        self._canvas.bind("<Button-4>",   lambda e: self._canvas.xview_scroll(-1, "units"))
        self._canvas.bind("<Button-5>",   lambda e: self._canvas.xview_scroll( 1, "units"))

        self._btns  = []
        self._tab_f = tab_f
        self._bold_f = tkfont.Font(family="Consolas", size=10, weight="bold")

        for i, name in enumerate(tab_names):
            btn = tk.Button(
                self._inner, text=name, font=self._tab_f,
                bg=TAB_INACT, fg=BTN_FG, relief="flat",
                padx=15, pady=5, cursor="hand2",
                activebackground=TAB_ACT, activeforeground="#fff",
                command=lambda i=i: on_select(i)
            )
            btn.pack(side="left", padx=3, pady=(2, 4))
            self._btns.append(btn)

    def _on_inner_configure(self, _=None):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self._canvas.itemconfig(self._win_id,
                                width=max(event.width, self._inner.winfo_reqwidth()))

    def _on_mousewheel(self, event):
        self._canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

    def highlight(self, active_idx):
        for j, tb in enumerate(self._btns):
            if j == active_idx:
                tb.configure(bg=TAB_ACT, fg="#fff", font=self._bold_f)
            else:
                tb.configure(bg=TAB_INACT, fg=BTN_FG, font=self._tab_f)


class ScrollableButtonGrid(tk.Frame):
    """A vertically scrollable grid of character buttons."""

    def __init__(self, parent, cols, mono_font, on_copy, **kwargs):
        super().__init__(parent, bg=PANEL, **kwargs)

        self._cols    = cols
        self._mono    = mono_font
        self._on_copy = on_copy
        self._btn_widgets = []

        self._canvas = tk.Canvas(self, bg=PANEL, highlightthickness=0, bd=0)
        self._sb = tk.Scrollbar(self, orient="vertical",
                                command=self._canvas.yview,
                                troughcolor=SB_TROUGH,
                                bg=SB_THUMB, activebackground=ACCENT,
                                highlightthickness=0, bd=0)
        self._canvas.configure(yscrollcommand=self._sb.set)
        self._canvas.pack(side="left", fill="both", expand=True)
        self._sb.pack(side="right", fill="y")

        self._inner = tk.Frame(self._canvas, bg=PANEL)
        self._win_id = self._canvas.create_window((0, 0), window=self._inner, anchor="nw")

        self._inner.bind("<Configure>", self._on_inner_configure)
        self._canvas.bind("<Configure>", self._on_canvas_configure)
        for w in (self._canvas, self._inner):
            w.bind("<MouseWheel>", self._on_mousewheel)
            w.bind("<Button-4>",   lambda e: self._canvas.yview_scroll(-1, "units"))
            w.bind("<Button-5>",   lambda e: self._canvas.yview_scroll( 1, "units"))

    def _on_inner_configure(self, _=None):
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self._canvas.itemconfig(self._win_id, width=event.width)

    def _on_mousewheel(self, event):
        self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _add_hover(self, btn):
        btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=BTN_HOV))
        btn.bind("<Leave>", lambda e, b=btn: b.configure(
            bg=BTN_BG if str(b["state"]) == "normal" else PANEL))
        btn.bind("<MouseWheel>", self._on_mousewheel)
        btn.bind("<Button-4>",   lambda e: self._canvas.yview_scroll(-1, "units"))
        btn.bind("<Button-5>",   lambda e: self._canvas.yview_scroll( 1, "units"))

    def load(self, chars):
        needed = len(chars)
        while len(self._btn_widgets) < needed:
            char_var = tk.StringVar(value=" ")
            idx = len(self._btn_widgets)
            r, c = divmod(idx, self._cols)
            btn = tk.Button(
                self._inner,
                textvariable=char_var,
                font=self._mono,
                width=7, height=2,
                bg=BTN_BG, fg=BTN_FG,
                relief="flat", cursor="hand2",
                activebackground=ACCENT,
                activeforeground="#fff",
                command=lambda cv=char_var: self._on_copy(cv.get())
            )
            btn.grid(row=r, column=c, padx=4, pady=4, ipadx=4, ipady=4)
            self._add_hover(btn)
            self._btn_widgets.append((btn, char_var))

        for i, (btn, char_var) in enumerate(self._btn_widgets):
            if i < needed:
                r, c = divmod(i, self._cols)
                char_var.set(chars[i])
                btn.grid(row=r, column=c, padx=4, pady=4, ipadx=4, ipady=4)
                btn.configure(state="normal", bg=BTN_BG)
            else:
                char_var.set(" ")
                btn.grid_remove()

        self._canvas.yview_moveto(0)


class KeypadApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Unitkeypad v1.2")
        self.configure(bg=BG)
        self.resizable(True, True)
        self.minsize(520, 340)

        self.mono    = tkfont.Font(family="Consolas", size=7)
        self.label_f = tkfont.Font(family="Consolas", size=9)
        self.tab_f   = tkfont.Font(family="Consolas", size=10, weight="bold")
        self.toast_f = tkfont.Font(family="Consolas", size=11, weight="bold")

        self._toast_id = None
        self._build_ui()
        self._switch_tab(0)

        self.update_idletasks()
        w, h = self.winfo_width(), self.winfo_height()
        x = (self.winfo_screenwidth()  - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"+{x}+{y}")

    def _build_ui(self):
        outer = tk.Frame(self, bg=BG, padx=2, pady=2)
        outer.pack(fill="both", expand=True)

        hdr = tk.Frame(outer, bg=BG, pady=10)
        hdr.pack(fill="x")
        tk.Label(hdr, text="⌨ UnitKeypad v1.2",
                 bg=BG, fg="#c8c8ff",
                 font=tkfont.Font(family="Consolas", size=13, weight="bold")
                 ).pack(side="left", padx=16)

        self._tab_bar = ScrollableTabBar(
            outer,
            tab_names=[name for name, _ in CHAR_GROUPS],
            on_select=self._switch_tab,
            tab_f=self.tab_f
        )
        self._tab_bar.pack(fill="x", padx=8, pady=(0, 4))

        self._grid = ScrollableButtonGrid(
            outer, cols=COLS,
            mono_font=self.mono,
            on_copy=self._copy,
            highlightbackground="#2a2a3a",
            highlightthickness=1
        )
        self._grid.pack(fill="both", expand=True, padx=10, pady=(0, 6))

        status = tk.Frame(outer, bg=BG, pady=6, padx=16)
        status.pack(fill="x")
        tk.Label(status,
                 text="Click any character to copy it to your clipboard",
                 bg=BG, fg=LABEL_FG, font=self.label_f
                 ).pack(side="left")

        self._toast = tk.Label(
            self, text="", bg=TOAST_BG, fg="#fff",
            font=self.toast_f, padx=18, pady=8, relief="flat"
        )

    def _switch_tab(self, idx):
        _, chars = CHAR_GROUPS[idx]
        self._grid.load(chars)
        self._tab_bar.highlight(idx)

    def _copy(self, ch):
        if ch.strip() == "":
            return
        pyperclip.copy(ch)
        self._show_toast(f"Copied  {ch}  to clipboard")

    def _show_toast(self, msg):
        self._toast.configure(text=msg)
        self.update_idletasks()
        tw = self._toast.winfo_reqwidth()
        ww = self.winfo_width()
        wh = self.winfo_height()
        self._toast.place(x=(ww - tw) // 2, y=wh - 54)
        self._toast.lift()
        if self._toast_id:
            self.after_cancel(self._toast_id)
        self._toast_id = self.after(1800, self._hide_toast)

    def _hide_toast(self):
        self._toast.place_forget()


if __name__ == "__main__":
    app = KeypadApp()
    app.mainloop()
