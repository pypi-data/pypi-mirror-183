from typing import Union
import base64
from io import BytesIO, StringIO

import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches

import IPython.display

import numpy as np

# verbergen van waarschuwingen van Matplotlib
import warnings
warnings.filterwarnings('ignore')

import pyco.basis
# import pyco.waarde
import pyco.lijst
import pyco.lijn
import pyco.venster

class pc:
    BasisObject = pyco.basis.BasisObject
    # Waarde = pyco.waarde.Waarde
    Lijst = pyco.lijst.Lijst
    Lijn = pyco.lijn.Lijn
    FiguurVenster = pyco.venster.FiguurVenster
    BestandsnaamVenster = pyco.venster.BestandsnaamVenster


class Figuur(pc.BasisObject):
    """
    Tekent een figuur met behulp van matplotlib bibliotheek.

    WERKWIJZE                   plaats functies achter elkaar
    f = Figuur(                 # configuratie
            breedte=7,
            hoogte=7,
        ).lijn(                 # onderdeel 1
            coordinaten=((2, 0), (3, 7)),
        ).fx(                   # onderdeel 2  etc.
            functie = lambda x: x**2,
            x = (-2, 3),
        ).plot()                # gebruik .plot() om weer te geven                   

    LIJN OBJECT             in plaats van tuple/list met coordinaten,
                            mag ook Lijn object invoeren
        Figuur().punt(
            coordinaten=Lijn([1,2],[3,4],[5,6])
        )
                            of twee pc.Lijst objecten
        Figuur().punt(
            coordinaten=(lijst1, lijst2)
        )

    CONFIGURATIE
        Figuur(
            breedte=7,
            hoogte=7,
            raster=True,
            legenda=True,
            titel='Kunst',
            x_as_titel='variabele $x$',
            y_as_titel='resultaat $y$',
            gelijke_assen=True,
            verberg_assen=False,
            x_as_log=False,
            y_as_log=False,
            spiegel_x_as=False,
            spiegel_y_as=False,
        )

    ONDERDELEN
        .lijn(
            coordinaten=((2, 0), (3, 7), (-2, 4), (2, 0)),
            breedte=3,
            kleur='red',   # None is auto kleur
            vullen=False,
            arcering='/',
            naam='dit is een lijn',
        )

        .punt(
            coordinaten=((2, 0), (3, 7), (-2, 4)),
            breedte=10,
            kleur='gold',   # None is auto kleur
            stijl='>',
            naam='dit zijn punten',
        )

        .tekst(
            coordinaten=((2, 0), (3, 7), (-2, 4)),
            teksten=('punt 1', 'punt 2', 'punt 3'),
            kleur='brown',   # None is auto kleur
            tekst_grootte='large', # {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
            tekst_font='sans-serif', # {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
            tekst_stijl='normal', # {'normal', 'italic', 'oblique'}
            tekst_gewicht='bold', # {'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
            hor_uitlijnen='center', # {'center', 'right', 'left'}
            vert_uitlijnen='center', # {'center', 'top', 'bottom', 'baseline', 'center_baseline'}
            roteren=30, # in graden
        )

        .kolom(
            coordinaten=((3, 8), (6, 4), (8, 1)),
            kleur='pink',   # None is auto kleur
            breedte=0.4,
            lijn_kleur='peru',
            lijn_breedte=2,
            naam='bar plot',
        )

        .fx(
            functie = lambda x: x**2 + 3*pc.sin(x),
            x = (-2, 3),
            breedte = 2,
            kleur = 'green',   # None is auto kleur
            naam = 'sinus parabool',
        )
        
    WEERGAVE FIGUUR
        f.plot()                # plot direct in notebook als pixel afbeelding
        f.plot_svg()            # plot direct in notebook als vector afbeelding
        f.plot_venster()        # plot in een popup venster

    OVERIG
        f.png_url               # data url encoded
        f.png_html              # HTML IMG code van PNG afbeelding (data url encoded)
        f.svg_html              # SVG code voor inline HTML gebruik
        f.bewaar_als_png()      # vraag bestandsnaam om op te slaan als PNG
        f.bewaar_als_svg()      # vraag bestandsnaam om op te slaan als SVG

    """

    def __init__(self,
                 breedte=8,
                 hoogte=8,
                 raster:bool=False,
                 legenda:bool=False,
                 titel:str='',
                 x_as_titel:str='',
                 y_as_titel:str='',
                 gelijke_assen:bool=False,
                 verberg_assen:bool=False,
                 x_as_log:bool=False,
                 y_as_log:bool=False,
                 spiegel_x_as:bool=False,
                 spiegel_y_as:bool=False):

        super().__init__()
        
        self.fig, self.ax = None, None
        
        self.breedte = breedte
        self.hoogte = hoogte

        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None

        self.marge_x = 0.05
        self.marge_y = 0.05

        self.maak_raster=raster
        self.maak_legenda=legenda

        self.titel = titel
        self.x_as_titel = x_as_titel
        self.y_as_titel = y_as_titel
        self.gelijke_assen = gelijke_assen
        self.verberg_assen = verberg_assen
        self.x_as_log = x_as_log
        self.y_as_log = y_as_log
        self.spiegel_x_as = spiegel_x_as
        self.spiegel_y_as = spiegel_y_as

        # if True:
        #     self.ax.spines['top'].set_visible(False)

        self._kleuren = plt.rcParams["axes.prop_cycle"]()

        self.alleen_lezen = False
        
        self._ax_plot_items = []

    def _check_coordinaten(self, coordinaten:Union[list, tuple, pc.Lijn]):
        """Controleert coordinaten en bepaalt globaal minimum en maximum."""
        if ((isinstance(coordinaten, list) or isinstance(coordinaten, tuple))
                    and len(coordinaten) == 2
                    and isinstance(coordinaten[0], pc.Lijst)
                    and isinstance(coordinaten[1], pc.Lijst)):
            coordinaten = tuple(zip(coordinaten[0].array, coordinaten[1].array))
        
        if not isinstance(coordinaten, list) and not isinstance(coordinaten, tuple):
            if isinstance(coordinaten, pc.Lijn):
                coordinaten.array.tolist()
            else:
                raise ValueError('coordinaten is geen Lijn, lijst of tupel')
        for coordinaat in coordinaten:
            if len(coordinaat) != 2:
                raise ValueError('coordinaat heeft minder of meer dan 2 elementen: {}'.format(coordinaat))

        x_waarden = [x for x, _ in coordinaten]
        y_waarden = [y for _, y in coordinaten]

        if self.min_x is not None:
            x_waarden = x_waarden + [self.min_x]
        if self.max_x is not None:
            x_waarden = x_waarden + [self.max_x]
        if self.min_y is not None:
            y_waarden = y_waarden + [self.min_y]
        if self.max_x is not None:
            y_waarden = y_waarden + [self.max_y]

        self.min_x = min(x_waarden)
        self.max_x = max(x_waarden)
        self.min_y = min(y_waarden)
        self.max_y = max(y_waarden)

        return coordinaten

    def _check_alleen_lezen(self):
        if self.alleen_lezen:
            raise Exception('figuur is al afgerond en is daardoor alleen-lezen')

    @property
    def volgende_kleur(self):
        return next(self._kleuren)["color"]

    def lijn(self,
             coordinaten:Union[list, tuple, pc.Lijn],
             breedte=1,
             kleur=None,
             vullen=False,
             arcering='',
             naam:str=None):
        """Trekt een lijn door middel van coordinaten."""

        self._check_alleen_lezen()
        
        kleur = self.volgende_kleur if kleur is None else kleur

        coordinaten = self._check_coordinaten(coordinaten)
        codes = [mpath.Path.MOVETO, *[mpath.Path.LINETO for _ in range(len(coordinaten)-1)]]
        path = mpath.Path(coordinaten, codes)
        patch = mpatches.PathPatch(path,
                                   linewidth=breedte,
                                   hatch=arcering,
                                   fill=vullen,
                                   color=kleur,
                                   label=naam)
        self._ax_plot_items.append(('add_patch', (patch,), dict()))
        return self

    def punt(self,
             coordinaten:Union[list, tuple, pc.Lijn],
             breedte=1,
             kleur='black',
             stijl='o',
             naam:str=None):
        """Plot punten door middel van coordinaten."""

        self._check_alleen_lezen()

        coordinaten = self._check_coordinaten(coordinaten)
        X = [x for x, _ in coordinaten]
        Y = [y for _, y in coordinaten]
        self._ax_plot_items.append(('scatter', (X, Y), dict(
            color=kleur,
            marker=stijl,
            s=breedte*30,
            label=naam)))
        return self

    def tekst(self,
             coordinaten:Union[list, tuple, pc.Lijn],
             teksten:Union[list, tuple],
             kleur=None,
             tekst_grootte:str='medium', # {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
             tekst_font:str='sans-serif', # {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
             tekst_stijl:str='normal', # {'normal', 'italic', 'oblique'}
             tekst_gewicht:str='normal', # {'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
             hor_uitlijnen:str='center', # {'center', 'right', 'left'}
             vert_uitlijnen:str='center', # {'center', 'top', 'bottom', 'baseline', 'center_baseline'}
             roteren:Union[float, int, str]=0): # float in degrees
        """Laat teksten zien op posities gegeven door coordinaten."""

        self._check_alleen_lezen()
        
        kleur = self.volgende_kleur if kleur is None else kleur

        coordinaten = self._check_coordinaten(coordinaten)
        X = [x for x, _ in coordinaten]
        Y = [y for _, y in coordinaten]
        for i, tekst in enumerate(teksten):
            x = X[i]
            y = Y[i]
            self._ax_plot_items.append(('text', (x, y), dict(
                    s=tekst,
                    color=kleur,
                    fontsize=tekst_grootte,
                    fontfamily=tekst_font,
                    fontstyle=tekst_stijl,
                    fontweight=tekst_gewicht,
                    horizontalalignment=hor_uitlijnen,
                    verticalalignment=vert_uitlijnen,
                    rotation=roteren)))
        return self

    def kolom(self,
             coordinaten:Union[list, tuple, pc.Lijn],
             kleur:str=None,
             breedte:Union[float, int]=0.8,
             lijn_kleur:str='black',
             lijn_breedte:Union[float, int]=0,
             naam:str=None):
        """Plot verticale kolommen door middel van coordinaten (positie, hoogte)."""

        self._check_alleen_lezen()
        
        kleur = self.volgende_kleur if kleur is None else kleur

        waardes = self._check_coordinaten(coordinaten)
        X = [x for x, _ in waardes]
        hoogtes = [h for _, h in waardes]
        self._ax_plot_items.append(('bar', (X,), dict(
                    height=hoogtes,
                    color=kleur,
                    width=breedte,
                    linewidth=lijn_breedte,
                    edgecolor=lijn_kleur,
                    label=naam)))
        return self

    def fx(self,
           functie,
           x:Union[list, tuple],
           breedte=1,
           kleur=None,
           naam:str=None,
           aantal_punten=100):
        """Plot een wiskundige functie bij bepaald domein."""

        self._check_alleen_lezen()
        
        kleur = self.volgende_kleur if kleur is None else kleur

        if len(x) != 2:
            raise ValueError('x waarde moet een lijst of tupel zijn met 2 getallen')

        X = np.linspace(x[0], x[1], aantal_punten)
        f = np.vectorize(functie)
        Y = f(X)

        self.min_x = min(self.min_x, x[0]) if self.min_x is not None else x[0]
        self.max_x = max(self.max_x, x[1]) if self.max_x is not None else x[1]
        self.min_y = min(self.min_y, min(Y)) if self.min_y is not None else min(Y)
        self.max_y = max(self.max_y, max(Y)) if self.max_y is not None else max(Y)

        self._ax_plot_items.append(('plot', (X, Y), dict(label=naam, color=kleur, linewidth=breedte)))
        return self

    def _afronden_figuur(self):
        """Rond figuur af."""
        if not self.alleen_lezen:
                
            self.fig, self.ax = plt.subplots(1, 1, figsize=(self.breedte, self.hoogte))

            if self.maak_raster:
                self.ax.axhline(y=0, color='darkgrey', linewidth=1.2)
                self.ax.axvline(x=0, color='darkgrey', linewidth=1.2)

            if self.titel != '':
                self.ax.set_title(self.titel)

            if self.x_as_titel != '':
                self.ax.set_xlabel(self.x_as_titel)

            if self.y_as_titel != '':
                self.ax.set_ylabel(self.y_as_titel)

            if self.gelijke_assen:
                self.ax.axis('equal')

            if self.verberg_assen:
                self.ax.set_axis_off()

            if self.x_as_log:
                self.ax.set_xscale('log')

            if self.y_as_log:
                self.ax.set_yscale('log')

            # plot alle data
            for plot_item in self._ax_plot_items:
                method_name, args, kwargs, = plot_item[0], plot_item[1], plot_item[2]
                getattr(self.ax, method_name)(*args, **kwargs)

            min_x = self.min_x if self.min_x is not None else 0
            max_x = self.max_x if self.max_x is not None else 1
            min_y = self.min_y if self.min_y is not None else 0
            max_y = self.max_y if self.max_y is not None else 1

            marge_x = (max_x - min_x) * self.marge_x
            marge_y = (max_y - min_y) * self.marge_y

            self.ax.axis([min_x - marge_x, max_x + marge_x, min_y - marge_y, max_y + marge_y])

            if self.maak_raster:
                self.ax.grid(color='grey', linestyle='-', linewidth=0.2)

            if self.maak_legenda:
                self.ax.legend()
                
            if self.spiegel_x_as:
                self.ax.invert_xaxis()
                
            if self.spiegel_y_as:
                self.ax.invert_yaxis()
                
        self.alleen_lezen = True

    def plot(self):
        """Rond figuur af en laat deze in IPython (notebook) als PNG afbeelding zien."""
        IPython.display.display(IPython.display.HTML(self.png_html))
        
    def plot_svg(self):
        """Rond figuur af en laat deze in IPython (notebook) als SVG afbeelding zien."""
        IPython.display.display(IPython.display.HTML(self.svg_html))

    def plot_venster(self):
        """Rond figuur af en laat deze in popup venster zien."""
        self._afronden_figuur()

        pyco.FiguurVenster(
            figuur=self,
            breedte=800,
            hoogte=600,
            titel='figuur' if self.titel == '' else self.titel,
        )

        plt.close(fig=self.fig)
    
    @property
    def png_url(self):
        """Genereer PNG data encoded url."""
        self._afronden_figuur()
        
        buf = BytesIO()
        self.fig.savefig(buf, format='png')
        data = base64.b64encode(buf.getbuffer()).decode('ascii')
        url = (f"data:image/png;base64,{data}")
        
        plt.close(fig=self.fig)
        return url

    @property
    def png_html(self):
        """Genereer PNG code voor inline gebruik IMG HTML."""
        return f"<img src='{self.png_url}'/>"

    def bewaar_als_png(self):
        """Vraag om bestandsnaam en bewaar afbeelding als PNG bestand."""
        self._afronden_figuur()
        
        bestandsnaam = pyco.BestandsnaamVenster(
            extensie='png',
            titel='Bewaren als PNG',
        ).bestandsnaam

        if bestandsnaam is not None:
            self.fig.savefig(bestandsnaam, format='png')
            
        plt.close(fig=self.fig)

    @property
    def svg_html(self):
        """Genereer SVG code voor inline gebruik HTML."""
        self._afronden_figuur()
        
        buf = StringIO()
        self.fig.savefig(buf, format='svg')
        data = buf.getvalue()
        # data heeft XML en DOCTYPE header; deze er afhalen (alleen SVG tags)
        data = '<svg ' + data.split('<svg ', 1)[1]
        
        plt.close(fig=self.fig)
        return data

    def bewaar_als_svg(self):
        """Vraag om bestandsnaam en bewaar afbeelding als SVG bestand."""
        self._afronden_figuur()
        
        bestandsnaam = pyco.BestandsnaamVenster(
            extensie='svg',
            titel='Bewaren als SVG',
        ).bestandsnaam

        if bestandsnaam is not None:
            self.fig.savefig(bestandsnaam, format='svg')
            
        plt.close(fig=self.fig)
