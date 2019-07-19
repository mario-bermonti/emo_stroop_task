
# Description

This is a Spanish Emotional Stroop task (EST) developed for a research project
conducted in a collaboration between the neurocognitive laboratory and the
Psychosocial laboratory at Ponce Health Sciences University. This project
compares people with a history of suicidal behavior vs a control
group (no history of suicidal behavior) on this and other tasks.

The EST was developed using Psychopy 3 builder but includes code
components. It can't be run with Psychopy 2 because it uses Unicode
characters (i.e., words with accents) and Psychopy crashes with this sort of
stimuli or doesn't display it correctly. It includes practice and experiment trials.

The EST was translated from the extended Stroop task (includes
instructions and practice trials) found in the demos that Psychopy provides. The
materials were translated and the trial document (csv file) was adapted.


## Practice trials

The EST includes 24 practice trials consisting of congruent word and colors.
The words presented are azul, rojo, and verde (i.e., Spanish words for
blue, red, and green) and are presented in colors blue, red, and green.
Participants respond by pressing:

-   f for red
-   j for green
-   "space bar" for blue


### Practice trial structure:

-   instructions
-   fixation cross for 1 sec
-   blank screen for .5 secs
-   the word is presented until a response is made
-   participant makes a response with the keyboard (f, j, space bar)
-   the participant receive feedback

Practice trials are organized into blocks of 6 words (two of each color) and
blocks are presented randomly.


## Experimental trials

There are 48 words from each valence (i.e., positive, negative, and neutral)
for a total of 144 words. Each word is presented only once. These blocks for
randomization are organized into 4 large experimental blocks of 36 trials
each. Participants are allowed 3 breaks to rest (one rest after completing
every 36 trials. The participant continues by pressing a key. Conditions are
balanced in terms of word length.


### Experimental trial's structure:

-   instructions
-   fixation cross for .5 sec
-   blank screen for .5 sec
-   word is presented until response is made
-   participant makes response with the keyboard (f, j, space bar)


### Technical details about blocks:

-   Trials (stimuli) are organized into blocks to get semi-randomization:
    -   16 blocks
    -   Each block has 9 trials: 3 words from each valence, with 1 word for
        each valence - color combination

The following table represents one block.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">text</th>
<th scope="col" class="org-left">letterColor</th>
<th scope="col" class="org-left">corrAns</th>
<th scope="col" class="org-left">condition</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">positive1</td>
<td class="org-left">blue</td>
<td class="org-left">j</td>
<td class="org-left">positive</td>
</tr>


<tr>
<td class="org-left">negative1</td>
<td class="org-left">blue</td>
<td class="org-left">j</td>
<td class="org-left">negative</td>
</tr>


<tr>
<td class="org-left">neutral1</td>
<td class="org-left">blue</td>
<td class="org-left">j</td>
<td class="org-left">neutral</td>
</tr>


<tr>
<td class="org-left">positive2</td>
<td class="org-left">green</td>
<td class="org-left">space</td>
<td class="org-left">positive</td>
</tr>


<tr>
<td class="org-left">negative2</td>
<td class="org-left">green</td>
<td class="org-left">space</td>
<td class="org-left">negative</td>
</tr>


<tr>
<td class="org-left">neutral2</td>
<td class="org-left">green</td>
<td class="org-left">space</td>
<td class="org-left">neutral</td>
</tr>


<tr>
<td class="org-left">positive3</td>
<td class="org-left">red</td>
<td class="org-left">f</td>
<td class="org-left">positive</td>
</tr>


<tr>
<td class="org-left">negative3</td>
<td class="org-left">red</td>
<td class="org-left">f</td>
<td class="org-left">negative</td>
</tr>


<tr>
<td class="org-left">neutral3</td>
<td class="org-left">red</td>
<td class="org-left">f</td>
<td class="org-left">neutral</td>
</tr>
</tbody>
</table>


## Procedure to prepare experiment

-   Trials need to be placed in a csv file (i.e. exp<sub>trials.csv</sub>) following the
    format presented above.
-   Blocks must be manually organized: each must have 9 trials, 3 for each condition,
    with 1 for every color (one from each condition - color pair)
-   The length of each block is specified as a range in the choose<sub>blocks.csv</sub> file
    -   Notes: psychopy starts counting from 0, so the first trial (row) is 0 and
        the range for every block starts as 1 less than the 'normal' value. Also,
        the last index is not included (so it has to be 1 more than would be expected)
        if we started counting from 0 (if its row number 8, it should be specified as 9,
        as seen below).

        Example:

        <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


        <colgroup>
        <col  class="org-center" />
        </colgroup>
        <thead>
        <tr>
        <th scope="col" class="org-center">block ranges</th>
        </tr>
        </thead>

        <tbody>
        <tr>
        <td class="org-center">0:9</td>
        </tr>


        <tr>
        <td class="org-center">9:18</td>
        </tr>
        </tbody>
        </table>


## Contact

If you have any questions don't hesitate to conctact me at [mbermonti@psm.edu](mailto:mbermonti@psm.edu).
If you find any errors or bugs, please open an issue and I'll work on it
as soon as possible.
