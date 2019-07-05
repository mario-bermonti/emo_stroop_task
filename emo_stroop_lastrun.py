#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on mar  2 jul 11:58:26 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.5'
expName = 'emo_stroop'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '01'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/MBP/Box Sync/PHSU/Design and stats consultation/Eliut Rivera/Suicide and Emotional Regulation Project/Emotional Stroop Task/emo_stroop_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "set_trial_blocks"
set_trial_blocksClock = core.Clock()
import random
import pandas as pd

# Specify the name of the file that specifies the 
# range of trials in each block
block_ranges = pd.read_csv('choose_blocks.csv')

# Randomize experiment blocks
block_ranges_exp = list(block_ranges.choose_blocks_exp)
random.shuffle(block_ranges_exp)

# Initialize components for Routine "instructPractice"
instructPracticeClock = core.Clock()
instr_practice = visual.TextStim(win=win, name='instr_practice',
    text='Recuerda, ignora la palabra.\n\nPresiona:\nf para letras rojas\nj para letras verdes\n"espacio" para letras azules\n\nVamos a comenzar con unos ejercicios de práctica\n\nPresiona cualquier tecla para comenzar',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_practice"
trial_practiceClock = core.Clock()
fixation_cross_practice = visual.TextStim(win=win, name='fixation_cross_practice',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
word_practice = visual.TextStim(win=win, name='word_practice',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start
# (empy string)
msg=''
text_feedback = visual.TextStim(win=win, name='text_feedback',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
black_screen = visual.Rect(
    win=win, name='black_screen',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instr_exp = visual.TextStim(win=win, name='instr_exp',
    text='¿Listo para comenzar el experimento real?\n\nRecuerda, ignora la palabra en sí misma.\n\nPresiona:\nf para letras rojas\nj para letras verdes\n"espacio" para letras azules\n\nPresiona cualquier tecla para comenzar',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_exp"
trial_expClock = core.Clock()
fixation_cross_exp = visual.TextStim(win=win, name='fixation_cross_exp',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
word_exp = visual.TextStim(win=win, name='word_exp',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
p_port = parallel.ParallelPort(address='0x0378')
print(p_port)
feedback_too_slow = visual.TextStim(win=win, name='feedback_too_slow',
    text='¡Muy lento!\n\n¡Intenta responder más rápido!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);


# Initialize components for Routine "ISI"
ISIClock = core.Clock()
black_screen = visual.Rect(
    win=win, name='black_screen',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "Rest"
RestClock = core.Clock()
# Initial value for the trial number
trial_exp_number = 0
text_rest = visual.TextStim(win=win, name='text_rest',
    text='¡Toma un descanso!\n\nPresiona cualquier tecla para comenzar',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='¡Completaste el experimento!\n\n¡Muchas gracias!',
    font='arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "set_trial_blocks"-------
t = 0
set_trial_blocksClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
set_trial_blocksComponents = []
for thisComponent in set_trial_blocksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "set_trial_blocks"-------
while continueRoutine:
    # get current time
    t = set_trial_blocksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in set_trial_blocksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "set_trial_blocks"-------
for thisComponent in set_trial_blocksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "set_trial_blocks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructPractice"-------
t = 0
instructPracticeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready_practice = event.BuilderKeyResponse()
# keep track of which components have finished
instructPracticeComponents = [instr_practice, ready_practice]
for thisComponent in instructPracticeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructPractice"-------
while continueRoutine:
    # get current time
    t = instructPracticeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_practice* updates
    if t >= 0.0 and instr_practice.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_practice.tStart = t
        instr_practice.frameNStart = frameN  # exact frame index
        instr_practice.setAutoDraw(True)
    
    # *ready_practice* updates
    if t >= 0.0 and ready_practice.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_practice.tStart = t
        ready_practice.frameNStart = frameN  # exact frame index
        ready_practice.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready_practice.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructPractice"-------
for thisComponent in instructPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_trials.csv'),
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_practice"-------
    t = 0
    trial_practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    word_practice.setColor(letterColor, colorSpace='rgb')
    word_practice.setText(text)
    resp_practice = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial_practiceComponents = [fixation_cross_practice, word_practice, resp_practice]
    for thisComponent in trial_practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial_practice"-------
    while continueRoutine:
        # get current time
        t = trial_practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross_practice* updates
        if t >= 0.0 and fixation_cross_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross_practice.tStart = t
            fixation_cross_practice.frameNStart = frameN  # exact frame index
            fixation_cross_practice.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross_practice.status == STARTED and t >= frameRemains:
            fixation_cross_practice.setAutoDraw(False)
        
        # *word_practice* updates
        if t >= 1.5 and word_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            word_practice.tStart = t
            word_practice.frameNStart = frameN  # exact frame index
            word_practice.setAutoDraw(True)
        
        # *resp_practice* updates
        if t >= 1.5 and resp_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_practice.tStart = t
            resp_practice.frameNStart = frameN  # exact frame index
            resp_practice.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp_practice.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp_practice.status == STARTED:
            theseKeys = event.getKeys(keyList=['f', 'j', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp_practice.keys = theseKeys[-1]  # just the last key pressed
                resp_practice.rt = resp_practice.clock.getTime()
                # was this 'correct'?
                if (resp_practice.keys == str(corrAns)) or (resp_practice.keys == corrAns):
                    resp_practice.corr = 1
                else:
                    resp_practice.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_practice"-------
    for thisComponent in trial_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_practice.keys in ['', [], None]:  # No response was made
        resp_practice.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp_practice.corr = 1;  # correct non-response
        else:
           resp_practice.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_loop (TrialHandler)
    practice_loop.addData('resp_practice.keys',resp_practice.keys)
    practice_loop.addData('resp_practice.corr', resp_practice.corr)
    if resp_practice.keys != None:  # we had a response
        practice_loop.addData('resp_practice.rt', resp_practice.rt)
    # the Routine "trial_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # Message if correct response
    if resp_practice.corr:#stored on last run routine
      msg=u"¡Correcto!"
    
    # Message if incorrect response
    else:
      msg=u"¡Error!"
    text_feedback.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [text_feedback]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_feedback* updates
        if t >= 0.0 and text_feedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_feedback.tStart = t
            text_feedback.frameNStart = frameN  # exact frame index
            text_feedback.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_feedback.status == STARTED and t >= frameRemains:
            text_feedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [black_screen]
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *black_screen* updates
        if t >= 0.0 and black_screen.status == NOT_STARTED:
            # keep track of start time/frame for later
            black_screen.tStart = t
            black_screen.frameNStart = frameN  # exact frame index
            black_screen.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if black_screen.status == STARTED and t >= frameRemains:
            black_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'practice_loop'

# get names of stimulus parameters
if practice_loop.trialList in ([], [None], None):
    params = []
else:
    params = practice_loop.trialList[0].keys()
# save data for this loop
practice_loop.saveAsExcel(filename + '.xlsx', sheetName='practice_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
practice_loop.saveAsText(filename + 'practice_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instruct"-------
t = 0
instructClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready_exp = event.BuilderKeyResponse()
# keep track of which components have finished
instructComponents = [instr_exp, ready_exp]
for thisComponent in instructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruct"-------
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_exp* updates
    if t >= 0 and instr_exp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_exp.tStart = t
        instr_exp.frameNStart = frameN  # exact frame index
        instr_exp.setAutoDraw(True)
    
    # *ready_exp* updates
    if t >= 0 and ready_exp.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_exp.tStart = t
        ready_exp.frameNStart = frameN  # exact frame index
        ready_exp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready_exp.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks_loop = data.TrialHandler(nReps=len(block_ranges_exp), method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks_loop')
thisExp.addLoop(blocks_loop)  # add the loop to the experiment
thisBlocks_loop = blocks_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
if thisBlocks_loop != None:
    for paramName in thisBlocks_loop:
        exec('{} = thisBlocks_loop[paramName]'.format(paramName))

for thisBlocks_loop in blocks_loop:
    currentLoop = blocks_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
    if thisBlocks_loop != None:
        for paramName in thisBlocks_loop:
            exec('{} = thisBlocks_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_exp_loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('exp_trials.csv', selection=block_ranges_exp.pop()),
        seed=None, name='trials_exp_loop')
    thisExp.addLoop(trials_exp_loop)  # add the loop to the experiment
    thisTrials_exp_loop = trials_exp_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_exp_loop.rgb)
    if thisTrials_exp_loop != None:
        for paramName in thisTrials_exp_loop:
            exec('{} = thisTrials_exp_loop[paramName]'.format(paramName))
    
    for thisTrials_exp_loop in trials_exp_loop:
        currentLoop = trials_exp_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_exp_loop.rgb)
        if thisTrials_exp_loop != None:
            for paramName in thisTrials_exp_loop:
                exec('{} = thisTrials_exp_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_exp"-------
        t = 0
        trial_expClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        word_exp.setColor(letterColor, colorSpace='rgb')
        word_exp.setText(text)
        resp_exp = event.BuilderKeyResponse()
        
        # keep track of which components have finished
        trial_expComponents = [fixation_cross_exp, word_exp, p_port, resp_exp, feedback_too_slow]
        for thisComponent in trial_expComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial_exp"-------
        while continueRoutine:
            # get current time
            t = trial_expClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross_exp* updates
            if t >= 0.0 and fixation_cross_exp.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_cross_exp.tStart = t
                fixation_cross_exp.frameNStart = frameN  # exact frame index
                fixation_cross_exp.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_cross_exp.status == STARTED and t >= frameRemains:
                fixation_cross_exp.setAutoDraw(False)
            
            # *word_exp* updates
            if t >= 1.5 and word_exp.status == NOT_STARTED:
                # keep track of start time/frame for later
                word_exp.tStart = t
                word_exp.frameNStart = frameN  # exact frame index
                word_exp.setAutoDraw(True)
            frameRemains = 1.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if word_exp.status == STARTED and t >= frameRemains:
                word_exp.setAutoDraw(False)
            # *p_port* updates
            if t >= 1.5 and p_port.status == NOT_STARTED:
                # keep track of start time/frame for later
                p_port.tStart = t
                p_port.frameNStart = frameN  # exact frame index
                p_port.status = STARTED
                win.callOnFlip(p_port.setData, int(trigger))
            frameRemains = 1.5 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if p_port.status == STARTED and t >= frameRemains:
                p_port.status = FINISHED
                win.callOnFlip(p_port.setData, int(0))
            
            # *resp_exp* updates
            if t >= 1.5 and resp_exp.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_exp.tStart = t
                resp_exp.frameNStart = frameN  # exact frame index
                resp_exp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp_exp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if resp_exp.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    resp_exp.keys = theseKeys[-1]  # just the last key pressed
                    resp_exp.rt = resp_exp.clock.getTime()
                    # was this 'correct'?
                    if (resp_exp.keys == str(corrAns)) or (resp_exp.keys == corrAns):
                        resp_exp.corr = 1
                    else:
                        resp_exp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *feedback_too_slow* updates
            if t >= 3.5 and feedback_too_slow.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedback_too_slow.tStart = t
                feedback_too_slow.frameNStart = frameN  # exact frame index
                feedback_too_slow.setAutoDraw(True)
            frameRemains = 3.5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedback_too_slow.status == STARTED and t >= frameRemains:
                feedback_too_slow.setAutoDraw(False)
            # Ends the routine if the participant has
            # taken more than 2 seconds to respond, after 
            # presenting a message that they took too
            # long to respond.
            
            # The absolute time from the start of the
            # routine has to be used (fixation cross 
            # + stim + keyboard + message).
            if t > 4.5:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_expComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_exp"-------
        for thisComponent in trial_expComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if p_port.status == STARTED:
            win.callOnFlip(p_port.setData, int(0))
        # check responses
        if resp_exp.keys in ['', [], None]:  # No response was made
            resp_exp.keys=None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               resp_exp.corr = 1;  # correct non-response
            else:
               resp_exp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_exp_loop (TrialHandler)
        trials_exp_loop.addData('resp_exp.keys',resp_exp.keys)
        trials_exp_loop.addData('resp_exp.corr', resp_exp.corr)
        if resp_exp.keys != None:  # we had a response
            trials_exp_loop.addData('resp_exp.rt', resp_exp.rt)
        
        # the Routine "trial_exp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [black_screen]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *black_screen* updates
            if t >= 0.0 and black_screen.status == NOT_STARTED:
                # keep track of start time/frame for later
                black_screen.tStart = t
                black_screen.frameNStart = frameN  # exact frame index
                black_screen.setAutoDraw(True)
            frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if black_screen.status == STARTED and t >= frameRemains:
                black_screen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "Rest"-------
        t = 0
        RestClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # Presents a break if trial number in  list
        # If number of trials changes, and the trial
        # at which the rest will be presented, 
        # the list needs to be updated with the
        # trial number after which there should be
        # a break
        if trial_exp_number not in [36, 72, 108]:
            continueRoutine = False
        
        # Needs to be updated after verifying
        # the trial number so it correctly
        # presents the break after the specified
        # trial
        trial_exp_number += 1
        ready_rest = event.BuilderKeyResponse()
        # keep track of which components have finished
        RestComponents = [text_rest, ready_rest]
        for thisComponent in RestComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Rest"-------
        while continueRoutine:
            # get current time
            t = RestClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_rest* updates
            if t >= 0.0 and text_rest.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_rest.tStart = t
                text_rest.frameNStart = frameN  # exact frame index
                text_rest.setAutoDraw(True)
            
            # *ready_rest* updates
            if t >= 0.0 and ready_rest.status == NOT_STARTED:
                # keep track of start time/frame for later
                ready_rest.tStart = t
                ready_rest.frameNStart = frameN  # exact frame index
                ready_rest.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            if ready_rest.status == STARTED:
                theseKeys = event.getKeys()
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Rest"-------
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_exp_loop'
    
    # get names of stimulus parameters
    if trials_exp_loop.trialList in ([], [None], None):
        params = []
    else:
        params = trials_exp_loop.trialList[0].keys()
    # save data for this loop
    trials_exp_loop.saveAsExcel(filename + '.xlsx', sheetName='trials_exp_loop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_exp_loop.saveAsText(filename + 'trials_exp_loop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed len(block_ranges_exp) repeats of 'blocks_loop'

# get names of stimulus parameters
if blocks_loop.trialList in ([], [None], None):
    params = []
else:
    params = blocks_loop.trialList[0].keys()
# save data for this loop
blocks_loop.saveAsExcel(filename + '.xlsx', sheetName='blocks_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
blocks_loop.saveAsText(filename + 'blocks_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksText.status == STARTED and t >= frameRemains:
        thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
