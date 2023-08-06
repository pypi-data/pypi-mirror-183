from math import sqrt

from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import fsolve

from open_channel.section import Section
from open_channel.constants import *


class RectangularSection(Section):
    def __init__(self):
        super().__init__()

        self._name = "Rectangular Section"
        self._note = ""
        self._b = 1.
        self._h = None
        self._Q = None

        self._law = None

        self._style = {"line_style": "-",
                       "line_thickness": 1,
                       "line_color": "Black",
                       "line_alpha": 1,
                       "line_order": 1,
                       "fill_color": "Cyan",
                       "fill_alpha": 1,
                       "fill_order": 1,
                       "font_size": 10,
                       "font_color": "Black",
                       "font_style": "normal",
                       "font_weight": "normal",
                       "arrow_style": "|-|",
                       "arrow_line_width": 1,
                       "arrow_line_style": "-",
                       "arrow_color": "Black",
                       "arrow_alpha": 1,
                       "arrow_order": 1}

    @property
    def name(self):
        """returns name"""
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    @property
    def note(self):
        """returns note"""
        return self._note

    @name.setter
    def note(self, note):
        if isinstance(note, str):
            self._note = note

    @property
    def b(self):
        """returns base width"""
        return self._b

    @b.setter
    def b(self, b):
        if isinstance(b, (int, float)):
            if 0 < b:
                self._b = b

    @property
    def h(self):
        """returns water height"""
        return self._h

    @property
    def Q(self):
        """returns discharge"""
        return self._Q

    @property
    def law(self):
        """returns law"""
        return self._law

    @property
    def style(self):
        return self._style
    
    @style.setter
    def style(self, style):
        if isinstance(style, dict):
            self._style = style

    @property
    def T(self):
        """returns Top Width"""
        if self._h is not None or self._Q is not None:
            return self._b
        else:
            return None

    @property
    def A(self):
        """returns Area"""
        if self._h is not None or self._Q is not None:
            return self._b * self._h
        else:
            return None

    @property
    def P(self):
        """returns Wetted Perimeter"""
        if self._h is not None or self._Q is not None:
            return self._b + 2 * self._h
        else:
            return None

    @property
    def R(self):
        """returns Hydraulic Radius"""
        if self._h is not None or self._Q is not None:
            return (self._b * self._h) / (self._b + 2 * self._h)
        else:
            return None

    @property
    def D(self):
        """returns Hydraulic Depth"""
        if self._h is not None or self._Q is not None:
            return self._h
        else:
            return None

    @property
    def H(self):
        """returns Energy"""
        if self._h is not None or self._Q is not None:
            return self._h + self.v**2 / (2 * g)
        else:
            return None

    @property
    def v(self):
        """returns velocity"""
        if self._h is not None or self._Q is not None:
            return self._Q / self.A
        else:
            return None

    @property
    def Fr(self):
        """returns Froude Number"""
        if self._h is not None or self._Q is not None:
            return self.v / (sqrt(g * self._h))    

    @property
    def xy(self):
        if self._h is not None or self._Q is not None:
            return [(0, self._h),
                    (0, 0),
                    (self._b/2, 0),
                    (self.b, 0),
                    (self._b, self._h)]

    def summary(self):
        if self._h != None:
            print("+--------------------------------------------------------------------------------+")
            print("|", f"{self._name}".center(78), "|")
            if self._note != "":
                print("|", f"{self._note}".center(78), "|")
            print("|", f"law : {self._law}".center(78), "|")
            print("+================================================================================+")
            print("|", "Base Width".center(18), "|", "Largeur de Base".center(24), "|", f"b = {round(self._b, 3)} m".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Water Height".center(18), "|", "Hauteur d'Eau".center(24), "|", f"h = {round(self._h, 3)} m".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Discharge".center(18), "|", "Débit".center(24), "|", f"Q = {round(self._Q, 3)} m^3/s".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Top Width".center(18), "|", "Largeur au Miroir".center(24), "|", f"T = {round(self.T, 3)} m".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Area".center(18), "|", "Surface Mouillée".center(24), "|", f"A = {round(self.A, 3)} m^2".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Wetted Perimeter".center(18), "|", "Périmètre Mouillé".center(24), "|", f"P = {round(self.P, 3)} m".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Hydraulic Radius".center(18), "|", "Rayon Hydraulique".center(24), "|", f"R = {round(self.R, 3)} m".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Hydraulic Depth".center(18), "|", "Profondeur Hydraulique".center(24), "|", f"D = {round(self.D, 3)} m".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Energy".center(18), "|", "Charge".center(24), "|", f"H = {round(self.H, 3)} m".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Velocity".center(18), "|", "Vitesse".center(24), "|", f"v = {round(self.v, 3)} m/s".center(30), "|")
            print("+--------------------+--------------------------+--------------------------------+")
            print("|", "Froude Number".center(18), "|", "Nombre de Froude".center(24), "|", f"Fr = {round(self.Fr, 3)}".center(30), "|")
            print("+--------------------------------------------------------------------------------+")

    def __repr__(self):
        return f"{self._name} | b = {self._b} m"

    def show(self):
        fig, ax = plt.subplots(figsize=(10, 15))
        plt.axis('off')
        ax.set_aspect('equal')

        x, y = self.coords()
        x.insert(0, 0)
        y.insert(0, self._h + self._h / 3)

        x.append(self.b)
        y.append(self._h + self._h / 3)

        line, = ax.plot(x, y)

        line.set_linestyle("-")
        line.set_color("Black")
        line.set_linewidth(1)
        line.set_alpha(1)
        line.set_zorder(1)

        fig.tight_layout()

    def get_h(self, **kwargs):
        if "law" not in kwargs.keys() or "Q" not in kwargs.keys():
            return None
        elif kwargs["law"] not in ["critical", "manning-strickler", "ferguson"]:
            return None
        elif not isinstance(kwargs["Q"], (int, float)):
            return None
        elif not 0 < kwargs["Q"]:
            return None
        else:
            if kwargs["law"] == "critical":
                self._law = kwargs["law"]
                self._Q = kwargs["Q"]
                self._h = (self._Q / (sqrt(g) * self._b))**(2./3.)

                return self._h

            elif kwargs["law"] == "manning-strickler":
                if "Ks" not in kwargs.keys() or "Sb" not in kwargs.keys() or "h0" not in kwargs.keys():
                    return None
                elif not isinstance(kwargs["Ks"], (int, float)) or not isinstance(kwargs["Sb"], (int, float)) or not isinstance(kwargs["h0"], (int, float)):
                    return None
                elif not 0 < kwargs["Ks"] or not 0 < kwargs["Sb"] or not 0 < kwargs["h0"]:
                    return None
                else:
                    self._law = kwargs["law"]
                    self._Q = kwargs["Q"]
                    Ks = kwargs["Ks"]
                    Sb = kwargs["Sb"]
                    h0 = kwargs["h0"]

                    f = lambda h: Ks * sqrt(Sb) * ((self._b * h)**(3./2.) / sqrt(self._b + 2 * h)) - self._Q
                    df = lambda h: Ks * sqrt(Sb) * (((3./2.) * self._b**(3./2.) * sqrt(h) * (self._b + 2*h) - (self._b * h)**(3./2.) ) / (self._b + 2*h)**(3./2.))

                    try:
                        h = fsolve(f, h0, fprime=df)
                        self._h = float(h[0])
                        return self._h
                    except:
                        return None

            elif kwargs["law"] == "ferguson":
                if "d84" not in kwargs.keys() or "Sb" not in kwargs.keys():
                    return None
                elif not isinstance(kwargs["d84"], (int, float)) or not isinstance(kwargs["Sb"], (int, float)):
                    return None
                elif not 0 < kwargs["d84"] or not 0 < kwargs["Sb"]:
                    return None
                else:
                    self._law = kwargs["law"]
                    self._Q = kwargs["Q"]
                    d84 = kwargs["d84"]
                    Sb = kwargs["Sb"]

                    v = self._Q
                    v /= 43.78 * self._b * sqrt(g * Sb * d84**3)
                    v = v**0.8214
                    v += 1
                    v = v**(-0.2435)
                    v *= (self._Q / (self._b * sqrt(g * Sb * d84**3)))**0.6
                    v *= 1.443 * sqrt(g * Sb * d84)

                    self._h = self._Q / (v * self._b)

                    return self._h

                    # f = lambda h: self._Q * d84 * sqrt(1 + 0.15 * (h / d84)**(5./3.)) - 2.5 * h**(5./2.) * self._b * sqrt(g * Sb)
                    # df = lambda h: (0.125*self._Q*d84*(h/d84)**1.66666666666667/(h*sqrt(0.15*(h/d84)**1.66666666666667 + 1)) - 6.25*self._b*h**1.5*sqrt(Sb*g))

                    # try:
                    #     h = fsolve(f, h0, fprime=df)
                    #     self._h = float(h[0])
                    #     return self._h
                    # except:
                    #     return None  
                    # 

                    # if self._Q / (self._b * sqrt(g * Sb * d84**3)) < 100:
                    #     p = 0.24
                    # else:
                    #     p = 0.31

                    # h = 0.015
                    # h *= d84
                    # h *= (self._Q / (self._b * sqrt(g * Sb * d84**3)))**(2*p)
                    # h /= p**2.5

                    # self._h = h
                    # return self._h

    def get_Q(self, **kwargs):
        if kwargs["law"] not in ["critical", "manning-strickler", "ferguson"]:
            return None
        elif not isinstance(kwargs["h"], (int, float)):
            return None
        elif not 0 < kwargs["h"]:
            return None
        else:
            if kwargs["law"] == "critical":
                self._law = kwargs["law"]
                self._h = kwargs["h"]
                self._Q = self._b * self._h**(3./2.) * sqrt(g)

                return self._Q
            
            elif kwargs["law"] == "manning-strickler":
                if "Ks" not in kwargs.keys() or "Sb" not in kwargs.keys():
                    return None
                elif not isinstance(kwargs["Ks"], (int, float)) or not isinstance(kwargs["Sb"], (int, float)):
                    return None
                elif not 0 < kwargs["Ks"] or not 0 < kwargs["Sb"]:
                    return None
                else:
                    self._law = kwargs["law"]
                    self._h = kwargs["h"]
                    self._Q = kwargs["Ks"] 
                    self._Q *= (self._b * self._h)**(3./2.)
                    self._Q *= sqrt(kwargs["Sb"])
                    self._Q /= sqrt(self._b + 2 * self._h)

                    return self._Q

            elif kwargs["law"] == "ferguson":
                if "d84" not in kwargs.keys() or "Sb" not in kwargs.keys() or "Q0" not in kwargs.keys():
                    return None
                elif not isinstance(kwargs["d84"], (int, float)) or not isinstance(kwargs["Sb"], (int, float)) or not isinstance(kwargs["Q0"], (int, float)):
                    return None
                elif not 0 < kwargs["d84"] or not 0 < kwargs["Sb"] or not 0 < kwargs["Q0"]:
                    return None
                else:
                    self._law = kwargs["law"]
                    self._h = kwargs["h"]
                    d84 = kwargs["d84"]
                    Sb = kwargs["Sb"]
                    Q0 = kwargs["Q0"]

                    # Q = self._b * sqrt(g * Sb * d84**3) * ((self._h * 0.24**2.5) / (0.015 * d84))**(1. / (2 * 0.24))

                    # if Q / (self._b * sqrt(g * Sb * d84**3)) < 100:
                    #     self._Q = Q
                    #     return self._Q
                    # else:
                    #     Q = self._b * sqrt(g * Sb * d84**3) * ((self._h * 0.31**2.5) / (0.015 * d84))**(1. / (2 * 0.31))
                    #     self._Q = Q
                    #     return self._Q

                    f = lambda Q: 1.443 * (Q / (self._b * sqrt(g * Sb * d84**3)))**0.6 * (1 + (Q / (43.78 * self._b * sqrt(g * Sb * d84**3)))**0.824)**(-0.2435) - (Q / (self._h * self._b * sqrt(g * Sb * d84)))
                    df = lambda Q: (-1 + 0.8658 * self._b * self._h * ( Q /(self._b * sqrt(Sb * d84**3 * g)))**0.6*sqrt(Sb * d84 * g) * (0.044859671915054*(Q/(self._b * sqrt(Sb * d84**3 * g)))**0.8214 + 1)**(-0.2435) / Q - 0.0129472068990062 * self._b * self._h * (Q / (self._b * sqrt(Sb * d84**3 * g)))**1.4214 * sqrt(Sb*d84 * g)*(0.044859671915054*(Q / (self._b * sqrt(Sb * d84**3 * g)))**0.8214 + 1)**(-1.2435) / Q)

                    try:
                        Q = fsolve(f, Q0, fprime=df)
                        self._Q = float(Q[0])
                        return self._Q
                    except:
                        return None

                    # try:
                    #     Q = brentq(f, Q0/10., Q0*10.)
                    #     self._Q = float(Q)
                    #     return self._Q
                    # except:
                    #     return None
