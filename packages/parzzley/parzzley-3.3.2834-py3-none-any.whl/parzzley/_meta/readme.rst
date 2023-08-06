============
Introduction
============

Please read how to make Parzzley ready for the first steps in :ref:`h_installation`.

First Steps
===========

Parzzley can run in graphical mode as well as in background mode. The latter one is designed for automated file synchronization, e.g. by periodical runs. It is described in :ref:`a later section<h_windowless>`.

For the first steps, start Parzzley in graphical mode. Either find the appropriate entry in your start menu or call :samp:`parzzley_gui`.

.. image:: maingui.png

It automatically creates an empty configuration file in :file:`~/.parzzley/parzzley.xml`. All changes you do in the Parzzley window will eventually be stored there.

It is easy to add a new synchronization now and let it run. This is great for configuration and for testing. For productive usage, it is recommended to run Parzzley in windowless mode. See the next chapter for more details.

You can set up your configuration entirely from the Parzzley window after start. Read more about the user interface in :ref:`h_graphicalconfig` and also about the :ref:`h_configmodel`.

Synchronization Model
=====================

This section describes how Parzzley proceeds in order to keep two filesystem locations synchronized, i.e. storing the same files. It can only explain how a usual configuration behaves. This behavior can be marginally or completely different once :ref:`h_customaspects` or other advanced features are used.

In order to keep two filesystem places in sync, Parzzley traverses those filesystem trees and operates per file:

- If a file is equally existing on both sides, it proceeds to the next.
- If a file only exists in one place, it decides whether to delete the one or to clone the other (by evaluating if the file existed before).
- If a file exists on both sides with different content, it checks which one is the fresher one (by evaluating the files' modification times) and updates the other. If both files changed since the last run, a :ref:`filesystem conflict<h_fsconflicts>` occurred.

It synchronizes the file content and a few metadata.

.. _h_windowless:

=================================
Using Parzzley In Windowless Mode
=================================

The Parzzley core component does not have any graphical interface but is designed to run completely in background without any user intervention.

The Parzzley command line tool :samp:`parzzley` runs the synchronization processes this way. It reads your Parzzley configuration file (or another other) and executes the synchronizations defined there.

The windowless mode is the recommended day-to-day mode. Parzzley is to be called in background in regular intervals (which should be short since Parzzley has an own interval logic). Add such a line to your :samp:`crontab` (or a similar 'scheduled task' in Windows or use whatever your OS provides for executing a command every few minutes):

.. code-block:: text

  */3 * * * * /usr/lib/parzzley/parzzley.py --sync ALL

Please adapt the Parzzley path to your system.

If you want to use another location for the configuration, create it at first by calling :samp:`parzzley --createconfig --configfile /some/other/dir/parzzley.xml` and adding ` --configfile /some/other/dir/parzzley.xml` to the crontab command. You can of course open and edit the resulting :file:`/some/other/dir/parzzley.xml` in the graphical configuration tool as well. Read :ref:`h_commandline` for more command line parameters.

You should also add a value :samp:`interval` on each for your synchronizations and set it to a time interval like :samp:`20m`. Otherwise they all actually will run every time Parzzley is called.

For details about return values of the Parzzley command line tool, see :py:class:`parzzley.runtime.returnvalue.ReturnValue`.

.. _h_graphicalconfig:

=======================
Graphical Configuration
=======================

The Parzzley main window gives an overview about all synchronizations and other stuff you have configured in the currently opened configuration file. You can open different ones at any time. Call :samp:`parzzley --createconfig --configfile /some/other/place/foo.xml` on command line for creating a fresh Parzzley configuration file in some place.

A fresh configuration is mostly empty and has just a Logger configured, so you get output information when syncing. You should not remove it, unless you really want to get rid of that its output. The user interface offers the 'Add item' action, which adds new parts to your configuration. A 'Sync Task' is what you typically would add in the beginning, while the other stuff is for more advanced cases and beyond this manual.

Once you have created a new sync task (sometimes also called: 'sync configuration', just 'sync', 'synchronization', ...) in Parzzley, you will see it in the main window. You can 'Configure' it, and clicking on its 'Properties' button offers all configuration details in a direct way (that should be used with care).

.. image:: mainguichange.png

Each action modifies your configuration in some way. The following explains the configuration of a sync task in detail.

.. rubric:: Configure

This opens a menu of possible configuration changes.

.. image:: changeguided.png

Those guided changes do not need deeper knowledge about Parzzley and often no reading of documentation.

.. rubric:: Remove sync

Removes an entire synchronization task.

.. rubric:: General, Preparation, Filesystem or Aspect level: Add parameter

Adds a name/value pair to the section.

Only add new parameters that are actually allowed for the underlying data structure. The :ref:`h_configmodel` section will explain more details.

.. rubric:: General or Filesystem level: Add aspect

Adds a new aspect to the filesystem or to the general section.

Only add new aspects that actually exist (either in :py:mod:`parzzley.aspect` or custom ones). The :ref:`h_configmodel` section will explain more details.

.. rubric:: Filesystem level: Add preparation

Adds a new preparation to the general section.

This is only used for exotic cases.

.. rubric:: Parameter, Preparation or Aspect level: Remove

Removes a section entirely.

Both potentially changes the behavior of this synchronization, so you should know what you are doing! Do not remove values that are required for the underlying data structure. The :ref:`h_configmodel` section will explain more details.

.. rubric:: Parameter level: Change value

Changes a value.

You should know about the allowed input values before you change something.

.. rubric:: Preparation, Aspect or Filesystem level: Change type

Changes the type of a preparation, aspect or filesystem.

This casts a filesystem or aspect to another type. Only choose a new type that actually exists (:py:mod:`parzzley.filesystem`, :py:mod:`parzzley.aspect` or custom ones). After you changed the type, it might be required to add and remove some values according to what the new data structure expects to get. The :ref:`h_configmodel` section will explain more details.

.. _h_configmodel:

===================
Configuration Model
===================

Beyond some configuration wizards, large parts of the graphical configuration directly reflect structures from the configuration file. So, for advanced usage, knowledge about the configuration file format is often required.

The configuration of Parzzley is (at least if you do not use it embedded in your own Python program) written in xml files. As default, the file :file:`parzzley.xml` in your home directory will be used. You may use a different one with the :samp:`--configfile` command line parameter.

A Parzzley configuration file contains configuration objects listed as sub nodes in the root node :samp:`parzzleyconfig`. There are different kinds of objects (e.g. loggers, synchronization tasks, ...), which can be seen in the different tag names in the xml.

.. hint::
   For most values in Parzzley configuration files, notations may contain references like :samp:`${FOO}`, which get replaced by that particular operating system environment variable.

Synchronization Tasks
=====================

Synchronization task configurations are the most interesting ones in most situations. They specify a pair of filesystem locations and a lot of optional additional stuff. The Parzzley engine will run the specified synchronization tasks as they are configured here.

A synchronization task configuration - using a :samp:`sync` tag in xml - is by far the most complex kind. An example can be seen in :file:`_meta/parzzley.xml.example`. The following shows and explains the formal structure:

.. code-block:: XML

  <?xml version="1.0" ?>
  <parzzleyconfig>
      <sync name="example" interval="5m" ...>
          <fs type="..." name="foo" ...>
              <aspect type="..." .../>
              <aspect type="..." .../>
          </fs>
          <fs type="..." name="bar" ...>
              <aspect type="..." .../>
              <aspect type="..." .../>
          </fs>
          <aspect type="..." .../>
          <aspect type="..." .../>
          <preparation type="..." .../>
          <preparation type="..." .../>
      </sync>
      ...
</parzzleyconfig>

A :samp:`sync` tag contains a name (e.g. used in log messages) and a synchronization interval. For more options, see :py:class:`parzzley.syncengine.sync.Sync`.

It contains two :samp:`fs` tags, which specify filesystem locations. They also have a name each and specify a filesystem location (local, ssh, or whatever is supported) for synchronization. See :py:mod:`parzzley.filesystem` for existing implementations.

Each :samp:`fs` tag may contain :samp:`aspect` tags. They control the synchronization behavior, since an aspect is a bunch of small program pieces that react on different events in the synchronization workflow. The complete synchronization functionality, even the builtin one, is part of aspects. See :py:mod:`parzzley.aspect` for existing implementations.

The :samp:`sync` tag may also contain :samp:`aspect` tags directly. Those aspects apply to all filesystems. It is the same as copying those tags into each :samp:`fs` tag.

It may also contain :samp:`preparation` tags. They specify some actions that must take place before the synchronization can take place. Mounting external filesystems is a very common example for this kind of actions. See :py:mod:`parzzley.preparation` for existing implementations.

Loggers
=======

Loggers can output Parzzley log messages in some way to some target. The configuration of one :samp:`logger` follows this structure:

.. code-block:: XML

  <?xml version="1.0" ?>
  <parzzleyconfig>
      <logger minseverity="debug" maxseverity="debug" ...>
          <out type="..." ... />
          <formatter type="..." .../>
      </logger>
      ...
  </parzzleyconfig>

It specifies a minimum and maximum severity that shall be logged (see :py:class:`parzzley.logger.logger.Severity`). It also contains a :samp:`formatter` configuration for an instance of :py:class:`parzzley.logger.formatter.abstractlogformat.Logformat` (formats the log message) and a :samp:`out` configuration for a :py:class:`parzzley.logger.loggerout.abstractloggerout.Loggerout` (actually does the output).

An example can be seen in :file:`_meta/parzzley.xml.example`.

See :py:mod:`parzzley.logger` for all available functionality.

Includes
========

A configuration file can include other ones. Those files have the same structure as primary configuration files and must be complete, including the :samp:`parzzleyconfig` xml root node.

A configuration file can be included with :samp:`include`, this way:

.. code-block:: XML

  <?xml version="1.0" ?>
  <parzzleyconfig>
      <include path="./some_other_file.xml"/>
      ...
  </parzzleyconfig>

.. _h_customaspects:

Custom Aspects
==============

A configuration file can bring the implementation for a custom aspect, which can then be used in some sync task configurations. Those implementations are provided in a :samp:`customaspect`:

.. code-block:: XML

  <?xml version="1.0" ?>
  <parzzleyconfig>
      <sync ...>
          ...
          <aspect type="DoSomething" />
      </sync>
      <customaspect name="DoSomething">
  from parzzley.aspect import *
  class DoSomething(Aspect):
      def __init__(self):
          Aspect.__init__(self)
      @hook("", "", "", event=SyncEvent.UpdateDir_Prepare)
      def sleepwhilebeginupdatedir(self, ea, fs, ctrl):
          do_something()
      </customaspect>
  </parzzleyconfig>

A custom aspect can be used for executing some custom code in some situations, e.g. for keeping EXIF tags of JPEG files clean or doing something with metadata tags of other media files.

Read the :ref:`h_customizing` section for details about implementing a custom aspect.

.. _h_pythonimports:

Python Imports
==============

Python Imports are used for customization. It allows importing arbitrary Python class or functions from any available module, so you can refer to it at other places. The configuration of one :samp:`pythonimport` follows this structure:

.. code-block:: XML

  <?xml version="1.0" ?>
  <parzzleyconfig>
      <pythonimport importfrom="my.mo.du.le.MyFilesystem" to="MyFilesystem" />
      ...
      <sync ...>
          <fs type="MyFilesystem" ...>
          ...
      </sync>
  </parzzleyconfig>

While :samp:`importfrom` must be a full name pointing to a Python object that is importable, :samp:`to` is just a bare name without dots!

.. _h_fsconflicts:

====================
Filesystem Conflicts
====================

Parzzley might encounter conflicts in synchronization runs. Those are situations with incompatible changes of one items on both sides. Those situations must be cleared manually by the user.

Since the Parzzley synchronization engine runs decoupled from user intervention, it just stores information about this conflict, so the user can decide later how to resolve it.

There is a graphical user interface available for manually resolving filesystem conflicts. Find it in your start menu, in the Parzzley overview, or execute :samp:`parzzley_infssync_manageconflicts_gui`.

There is also a command line tool available as :samp:`parzzley_infssync_manageconflicts`. It is designed for scripted usage. Just start it for getting further details.

After a conflict occurs, those tools can be used to manually resolve each issue. These tools store a conflict resolution information, which is applied when the synchronization task runs the next time. They do not execute any synchronization action directly.

.. image:: conflict.png

=========
Reporting
=========

Parzzley collects some process and telemetry information while it executes your synchronization tasks. This includes the execution logs for each run and performance data.

There is a convenient user interface for inspecting those data. Find it in your start menu, in the Parzzley overview, or execute :samp:`parzzley_report_gui`.

.. image:: reporting.png

.. _h_customizing:

====================
Customizing Parzzley
====================

General Workflow Overview
=========================

The following describes how the inner parts of Parzzley work together. This knowledge is very helpful for planning and implementing a customization.

For each :samp:`<sync>` in your configuration, the Parzzley engine will create and configure one instance of :py:class:`parzzley.syncengine.sync.Sync`. If it is not skipped (e.g. because it was already executed less time ago than the :samp:`interval` defines), the engine tries to prepare the execution.

Preparing a synchronization means activating all :samp:`<preparation>` specified for this synchronization task. This can mount filesystems or whatever is needed for bringing an environment in place, which is required for the actual synchronization to run. Each :samp:`preparation` is one instance of a subclass of :py:class:`parzzley.preparation.abstractpreparation.Preparation`, which provides the implementation for activating a preparation before synchronization, for deactivating it afterwards and for status checks.

If the synchronization task is successfully prepared, the actual sync operation begins. The sync operation iterates over whatever it can find in your filesystems and just triggers certain events. Without anything more, it would not do anything (and, technically, it would not even iterate that much - but let's forget that for now). The complete synchronization behavior comes with a bunch of small pieces of program code that react on those events. Even the builtin Parzzley synchronization behavior is implemented as aspects (which also means that you can completely get rid of it by not listing those aspects in your sync configuration).

Those event handlers are added to the pipe by means of some :samp:`<aspect>`. Each specified aspect (either within one :samp:`<filesystem>` or directly within the :samp:`<sync>`) brings an instance of a subclass of :py:class:`parzzley.aspect.abstractaspect.Aspect`, which registers one or more event handlers to the synchronization pipe. One aspect typically implements a certain piece of behavior (which often needs to react on more than only one event).

Intermediate summary: A synchronization task itself is not an interesting thing. It will just fly over your files doing nothing. It can be enriched with some preceding or subsequent actions by means of a :samp:`preparation`. But all the interesting synchronization behavior comes with event handlers. Those event handlers are bundled in some :samp:`aspect`.

The following description gives a more detailed overview of how Parzzley would fly over your filesystem and which events are triggered on that flight (i.e. which junction points exist, where aspects can hook in for own logic). For most events, additional information is available in the developer documentation.

- At the very beginning of the synchronization run (directly after it is prepared), :py:data:`parzzley.syncengine.common.SyncEvent.BeginSync` is triggered.

  .. image:: beginsync.png

- Afterwards it starts the synchronization of the root directory. Synchronization of a directory (the root one and all the other ones) executes those steps:

  - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateDir_Prepare` is triggered for preparing the directory synchronization.

    .. image:: beginsyncdir.png

  - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateDir_ListDir` is triggered for collecting a list of all direct child entries (files, subdirectories, ...) in that directory.

    .. image:: listdir.png

  - Afterwards, Parzzley iterates over all the listed child entries that were listed and synchronizes this entry. Each entry synchronization executes those steps:

    - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateItem_BeforeElectMaster` is triggered for preparing the next step.

      .. image:: beforeelectmaster.png

    - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateItem_ElectMaster` is triggered for electing the master filesystem. This is the filesystem that contains the 'right' version of that item. All the other filesystems are meant to get updated according to this version. The result of the election could be to skip all the other steps for this child entirely. It can also select a non-existing location (which typically leads to deletion later on).

      .. image:: electmaster.png

    - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateItem_CheckConflicts` is triggered for checking if a conflict exists between the master filesystem and any other one.

      .. image:: checkconflicts.png

    - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateItem_ResolveConflicts` is triggered for resolving those conflicts, if conflicts appeared.

      .. image:: resolveconflicts.png

    - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateItem_SkippedDueConflicts` is triggered if conflicts appeared and could not be resolved. In that situation, after triggering this event, some of the next steps are skipped and processing resumes at :samp:`UpdateItem_AfterUpdate` (see below).

      .. image:: skippeddueconflicts.png

    - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateItem_Update_Prepare` is triggered for preparing the actual updating.

      .. image:: update.png

    - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateItem_Update_ExistsInMaster` is triggered for actually updating an entry, if it exists in the master filesystem (typically in order to copy it to the other filesystems). If the entry is a directory, this also starts synchronizing this directory by means of the workflow described here (beginning above). This is realized by :py:class:`parzzley.aspect.baseinfrastructure.BaseInfrastructure`, which is always implicitely included in each synchronization configuration.

      .. image:: syncexistinmasterdir.png

    - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateItem_Update_NotExistsInMaster` is triggered for actually updating an entry, if it does not exist in the master filesystem (typically in order to remove it from the other filesystems).

    - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateItem_AfterUpdate` is triggered after the entry was synchronized.

      .. image:: afterupdate.png

  - :py:data:`parzzley.syncengine.common.SyncEvent.UpdateDir_AfterUpdate` is triggered after the directory was synchronized.

    .. image:: afterupdatedir.png

- At the end of the synchronization, :py:data:`parzzley.syncengine.common.SyncEvent.EndSync` is triggered.

  .. image:: endsync.png

Whenever an event occurs, all registered event handlers are executed. Each event handler execution takes place on top (or: is associated with) one of your specified filesystems. Each event handler typically does its work in that particular filesystem. If an aspect that provides a certain event handler is specified in a :samp:`filesystem`, it will be executed exactly for that filesystem. If it is directly specified in the :samp:`sync`, it will be executed once for each filesystem.

There is a mechanism for ordering the execution of the event handlers within one event. Please read :py:meth:`parzzley.syncengine.sync.Sync.executeevent` for more details about the ordering and more about the internals.

Customizable Parts
==================

If you want to override or enhance some parts of the default behavior, read the following parts:

- :py:class:`parzzley.aspect.abstractaspect.Aspect` is the base class of your implementation if you want to develop a part of logical behavior, like 'copy a file to somewhere in some situations'. Inspect the sources in :py:mod:`parzzley.aspect` for lots of practical examples. Read also about how to put your :ref:`h_customaspects` to a configuration.

- :py:class:`parzzley.filesystem.abstractfilesystem.Filesystem` is the base class of your own filesystem implementation, which allows usage of a filesystem that is neither the local one nor another support one. Insect the sources in :py:mod:`parzzley.filesystem` for examples.

- :py:class:`parzzley.preparation.abstractpreparation.Preparation` is the base class for sync preparations, which will be enabled before the synchronization runs and disabled afterwards by the Parzzley engine. One typical use case is mounting a remote filesystem. Inspect the sources in :py:mod:`parzzley.preparation` for examples.

High Level Customization
========================

The :py:class:`parzzley.aspect.highlevelcustomization.HighLevelCustomization` aspect allows to include Python code pieces from somewhere in the synchronization directory tree at defined places into the synchronization behavior.

This is very convenient for including some automation tasks, e.g. automatically converting some kinds of files whenever the appear or reacting in any other custom way to filesystem updates.

Include this aspect to your configuration in order to use this feature. The graphical interface has a guide for it as well.

Python Imports
==============

It is possible to implement own stuff in external Python modules and use those classes and functions from within the configuration (e.g. as a different filesystem type). Specify a :ref:`Python Import<h_pythonimports>` for such a class or function.

.. _h_commandline:

======================
Appendix: Command Line
======================

The Parzzley command-line tool understands this syntax:

.. code-block:: sh

  parzzley [options]*

Options can be some of the following:

- :samp:`--sync [syncname]` : Runs the synchronization of :samp:`syncname`. Use :samp:`ALL` for :samp:`syncname` in order to run all synchronizations.

- :samp:`--listsyncs` : Lists all available synchronization configurations.

- :samp:`--datadir [dirpath]` : Uses :samp:`dirpath` as control data storage directory instead of the default one (:file:`~/.parzzley`).

- :samp:`--configfile [configfile]` : Uses configuration file :samp:`configfile` instead of the default one (:file:`~/.parzzley/parzzley.xml`).

- :samp:`--createconfig` : Creates a fresh configuration file (can be combined with :samp:`datadir`).

- :samp:`--forcesync [syncname]` : Marks the synchronization :samp:`syncname` for forceful synchronization, even if the time interval is not elapsed yet. Can be used more than once.

- :samp:`--lock [pid]` : Just acquires the lock, so no other synchronization run will actually do anything until you :samp:`unlock`. Used for backup. Without a pid, the lock must be unlocked and refreshed every 10 minutes!

- :samp:`--unlock` : Releases a lock acquired with :samp:`--lock`.

.. _h_installation:

======================
Appendix: Installation
======================

Install Parzzley via the installation package for your environment, if a suitable one exists for download. This also takes care of installing dependencies and doing preparation (unless mentioned otherwise in the installation procedure). After the installation, you can skip the rest of this section.

Source Code Archive
===================

Use the source code archive as fallback. Extract it to a location that is convenient to you (Windows users need an external archive program; for example the great '7-Zip' tool). Also take a look at the :ref:`Dependencies<_dependencies>` for external stuff you need to install as well.

It is highly recommended to also establish a command line link or alias for :file:`parzzley/parzzley.py` so you just have to type :samp:`parzzley` (:samp:`ln -s ...parzzley/parzzley.py /usr/local/bin/parzzley` on Unix or any other operating system specific way). Do the same for :file:`parzzley/parzzley_gui.py`, :file:`parzzley/parzzley_infssync_manageconflicts.py` and :file:`parzzley/parzzley_infssync_manageconflicts_gui.py`. This is according to what the installation packages do and required for executing the exact same commands as used in this manual (otherwise you must substitute the full name for the short command names in this manual).
