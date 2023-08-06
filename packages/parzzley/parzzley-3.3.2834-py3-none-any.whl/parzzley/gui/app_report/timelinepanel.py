# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

import datetime
import math
import os

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GObject
from gi.repository import GLib
from gi.repository import Gtk

from parzzley.gui.helpers import tr
import parzzley.gui.gtk
import parzzley.gui.report


_mydir = os.path.dirname(__file__)


class Timeline(Gtk.DrawingArea):
    __gtype_name__ = "Timeline"

    def __init__(self, **kwargs):
        self.__begintime = datetime.datetime.now()
        self.__endtime = datetime.datetime.now()
        self.__indicatorsteptime = datetime.timedelta(days=1)
        super().__init__(**kwargs)
        self.connect("draw", self.__draw)

    def do_get_preferred_height(self):
        return 180, 180

    @GObject.Property(type=float)
    def begintime(self) -> float:
        return self.__begintime.timestamp()

    @begintime.setter
    def begintime(self, d: float):
        self.__begintime = datetime.datetime.fromtimestamp(d)
        self.queue_draw()

    @GObject.Property(type=float)
    def endtime(self) -> float:
        return self.__endtime.timestamp()

    @endtime.setter
    def endtime(self, d: float):
        self.__endtime = datetime.datetime.fromtimestamp(d)
        self.queue_draw()

    @GObject.Property(type=float)
    def indicatorsteptime(self) -> float:
        return self.__indicatorsteptime.total_seconds()

    @indicatorsteptime.setter
    def indicatorsteptime(self, d: float):
        self.__indicatorsteptime = datetime.timedelta(seconds=d)
        self.queue_draw()

    def __draw(self, widget, context):
        fullwidth, fullheight = widget.get_allocated_width(), widget.get_allocated_height()
        altcolor = self.get_style_context().get_color(Gtk.StateFlags.LINK)
        context.set_source_rgba(altcolor.red, altcolor.green, altcolor.blue, 0.7)
        sdate = self.__begintime
        context.set_font_size(self.get_style_context().get_property("font-size", Gtk.StateFlags.NORMAL))
        lineheight = context.font_extents()[2]
        textshmargin, textsvmargin = 5, 5
        textsfullwidth = fullwidth - 2 * lineheight - 2 * textshmargin
        lastday = None
        context.set_line_width(2)
        context.move_to(0, 0.2 * fullheight)
        context.line_to(fullwidth, 0.2 * fullheight)
        context.stroke()
        context.set_line_width(4)
        context.save()
        while sdate <= self.__endtime:
            x = (sdate.timestamp() - self.begintime) / (self.endtime - self.begintime)
            context.move_to(x * fullwidth, 0.2 * fullheight)
            context.line_to(x * fullwidth, 0.3 * fullheight)
            context.stroke()
            axislbltext1 = sdate.strftime("%x") if (lastday != sdate.date()) else ""
            txtx = x * textsfullwidth + lineheight + textshmargin
            context.move_to(txtx, textsvmargin + 0.3 * fullheight + context.text_extents(axislbltext1).width)
            context.rotate(-math.pi / 2)
            context.show_text(axislbltext1)
            context.restore()
            context.save()
            axislbltext2 = datetime.datetime.fromtimestamp(int(sdate.timestamp())).strftime("%X")
            context.move_to(txtx + lineheight,
                            textsvmargin + 0.3 * fullheight + context.text_extents(axislbltext2).width)
            context.rotate(-math.pi / 2)
            context.show_text(axislbltext2)
            context.restore()
            context.save()
            lastday = sdate.date()
            sdate += self.__indicatorsteptime
        context.restore()


@Gtk.Template.from_file(f"{_mydir}/timelinepanel.ui")
class TimelinePanel(Gtk.Box):
    __gtype_name__ = "TimelinePanel"

    slctimeinterval = Gtk.Template.Child()
    pnltimelines = Gtk.Template.Child()
    resizedetector = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        parzzley.gui.gtk.load_css(f"{_mydir}/timelinepanel.css")
        self.__dir = None
        self.slctimeinterval.connect("changed", self.__refresh)
        self.resizedetector.connect("configure-event", lambda *_: GLib.idle_add(self.__refresh))

    def _populate(self, dirpath):
        self.__dir = dirpath
        self.__refresh()

    def __refresh(self, *_):
        for oldchild in self.pnltimelines.get_children():
            self.pnltimelines.remove(oldchild)
        intervalcode = self.slctimeinterval.props.active_id
        nextmidnight = datetime.datetime.fromordinal((datetime.date.today() + datetime.timedelta(days=1)).toordinal())
        if intervalcode == "month":
            timelinescount = 8
            timelinespan = datetime.timedelta(days=7)
            indicatorsteptime = datetime.timedelta(days=1)
            endtime = nextmidnight
        elif intervalcode == "week":
            timelinescount = 7
            timelinespan = datetime.timedelta(days=1)
            indicatorsteptime = datetime.timedelta(hours=4)
            endtime = nextmidnight
        elif intervalcode == "day":
            timelinescount = 8
            timelinespan = datetime.timedelta(hours=3)
            indicatorsteptime = datetime.timedelta(minutes=30)
            endtime = nextmidnight
        elif intervalcode == "hour":
            timelinescount = 6
            timelinespan = datetime.timedelta(minutes=10)
            indicatorsteptime = datetime.timedelta(minutes=2)
            endtime = datetime.datetime.now().replace(second=0, microsecond=0) + datetime.timedelta(minutes=1)
        else:
            raise RuntimeError(f"bad intervalcode: {intervalcode}")
        fullwidth = self.pnltimelines.get_allocation().width
        events = parzzley.gui.report.try_load_log_from_syncdir(self.__dir)
        def popover(e, ebtn):
            def handler(*_):
                w = Gtk.Popover()
                strfrom, strto = tr("from"), tr("to")
                strfailed, strfinished = tr("failed prematurely"), tr("finished")
                Gtk.Label(label=(
                    f"{strfrom} {datetime.datetime.fromtimestamp(int(e.begintime.timestamp())).strftime('%c')}\n"
                    f"{strto} {datetime.datetime.fromtimestamp(int(e.endtime.timestamp())).strftime('%c')}\n\n"
                    f"{strfailed if e.crashed else strfinished}\n\n{e.syncrun}"), parent=w, margin=10).show()
                w.props.relative_to = ebtn
                w.popup()
            return handler
        widgets = []
        for _ in list(range(timelinescount, 0, -1)):
            begintime = endtime - timelinespan
            overlay = Gtk.Overlay()
            widgets.append(overlay)
            timeline = Timeline(begintime=begintime.timestamp(), endtime=endtime.timestamp(), parent=overlay,
                                indicatorsteptime=indicatorsteptime.total_seconds())
            fullheight = timeline.do_get_preferred_height()[0]
            for event in events:
                if not (event.endtime < begintime or event.begintime > endtime):
                    relbegin = (event.begintime - begintime) / (endtime - begintime)
                    relend = (event.endtime - begintime) / (endtime - begintime)
                    eventbtn = Gtk.Button(width_request=fullwidth*(relend-relbegin), height_request=0.16*fullheight,
                                          margin_left=fullwidth*relbegin, margin_top=0.05*fullheight,
                                          halign=Gtk.Align.START, valign=Gtk.Align.START)
                    eventbtn.connect("clicked", popover(event, eventbtn))
                    eventbtn.get_style_context().add_class("syncevent")
                    eventbtn.get_style_context().add_class("notsuccessful" if event.crashed else "successful")
                    overlay.add_overlay(eventbtn)
            endtime = begintime
        for widget in reversed(widgets):
            self.pnltimelines.add(widget)
        self.pnltimelines.show_all()
