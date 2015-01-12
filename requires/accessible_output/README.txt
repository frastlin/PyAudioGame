=====================================================
 The accessible_output library
=====================================================

:Author: Christopher Toth <Q@Qwitter-Client.net>
:Date: $Date: 06-27-2011 02:00:00 -0400 (Mon, Jun 27, 2011)
:Web site: http://www.qwitter-client.net/
:Copyright: 2011


.. contents::

============
Introduction
============

Accessible Output provides a standard way for developers to output text in either speech or braille using a preinstalled screen reader.  Using accessible_output makes creating self-voicing applications extremely easy.  

===========
Basic Usage
===========
Using accessible output is extremely simple::

    #!/usr/bin/env python
    from accessible_output import speech
    s = speech.Speaker() #Will load the default speaker.
    s.output("The message to speak")

==============
Speech Outputs
==============

* JAWS for Windows
* Window Eyes
* Dolphin Screen Readers newer than v11.
* NVDA 2010.1 or newer
* System Access and System Access To Go
* Microsoft sapi 5 speech
* Speech Dispatcher
* Apple VoiceOver

===============
Braille Outputs
===============


* JAWS for Windows
* Window Eyes
* NVDA
* System Access and System Access To Go
