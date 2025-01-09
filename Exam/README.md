# ADA Final Exam

This repository contains the final exam for Applied Data Analysis (CS-401).

The questions and the data will be made available to you at 15:15 on Tuesday January 14th, 2025.

All the logistical details, rules, and guidelines for the exam are stated below.

Additionally, to iron out critical logistical aspects, such as execution environment setup, sharing of high-level rules, and submission process of your solved exam, we would like each of you to participate in a dry run of the exam. Please see the [dry-run instructions](#Dry-run-Instructions) section at the bottom of this document for details.

## Conda Environment
We have prepared a python environment, named `adaexam`, with all the Python packages that you might need for the exam. You can install it with the following command:   

```shell
conda create -n ada_exam_2024  python=3.10 -y
conda activate ada_exam_2024
pip install -r requirements.txt
```

*Note-1: Not all packages will be needed for the exam, but we have included them for your convenience.*
*Note-2: No additional packages are needed to run the solutions notebook.*

We strongly recommend that you set up this environment and use it for the exam. Different versions of packages may lead to compatibility issues, and we will not be able to provide support for such issues during the exam. If your solution is slightly different from the expected solution due to package version differences, you will be penalized to some extent.

## Timeline

**Exam date:** Tuesday, January 14th, 2025   
**Exam start:** 15:15 (CET/UTC+1h)   
**Exam end:** 18:15 (CET/UTC+1h)   

## Seats

The exam will take place in the following rooms:
CE11, CE12, CE13, CE14, CE16, CM1, CM2, CM3, CM4, CO1, CO2, CO3

The seating plan will be published the day before the exam and also put up on the doors of the rooms on the day of the exam.

## Submission

* You need to submit your solutions in the form of a single Jupyter Notebook (`.ipynb` file) to [this Google form (will be activated on the day of exam)](https://forms.gle/52qASNex6khKaGx58) before the end of the exam.**Late submissions will not be accepted.** 
* After submission, you can correct 'typos' in your name using the "edit response" option, however, the uploaded 'ipynb' file cannot be modified. If you need to modify the ‘ipynb’ file, please create a new submission using the "Submit another response" option.
* It's allowed to upload submission multiple times (using the "Submit another response" option) before the deadline at 18:15. So, it is recommended to submit a partial solution during the exam and then overwrite it with the final one before the deadline. We will only consider the **latest** submission before the deadline.
* For students **with** an EPFL sciper number:
   * Your file has to be named as "YourSCIPERNumber.ipynb". For example, if your SCIPER number is '123456', please name your file as '123456.ipynb'.   
* For students **without** an EPFL sciper number:
   * Your file has to be named (in *titlecase*) as "YourFirstName_YourLastName.ipynb". For example, if your first name is 'Abc', and last name is 'Xyz', please name your file as 'Abc_Xyz.ipynb'.   
* We recommend that you test the dry-run submission at [this dry run submission form](https://forms.gle/bYxSEzTozsfLdQpe8) to ensure that you can submit the exam successfully.
* If you face any urgent issues with the submission process, send your submission to `silin.gao@epfl.ch`. However, this should be considered as a last resort, and we will penalize students who use this option without a valid reason.

A few additional notes:

- We won't grade your exam if the file is not properly named, thus, be extra careful in this regard
- The Google form upload utility might automatically append the name on your EPFL account to the filename provided by you, thus, don't be alarmed if this happens; it’s fine. For instance, if your name on the EPFL account is 'Abc Xyz' and you upload the file '123456.ipynb', it might be renamed to '123456 - Abc Xyz.ipynb'
- Two-factor authentication might be required for Google account with EPFL email addresses. Please make sure your account is logged in a browser before the exam starts to avoid any last-minute issues with Two-factor authentication.
- We recommend that you submit the google form with EPFL account credentials, but you can also use a personal Google account. However, make sure your epfl email address is correctly filled in the form.
- You can opt the "Send me a copy of my responses" option in the form to receive an email confirmation of your submission. This is optional, but it can be used as a backup confirmation of your submission.

## Dry-run Instructions

Complete the following steps for a smooth exam experience on the day of the exam:

1. Carefully read and familiarize yourself with all the aforementioned rules and instructions.
2. Set up the `ada_exam_2024` [conda environment](#Conda-Environment).
3. Execute all the cells of `exam_dryrun.ipynb` in Jupyter with `ada_exam_2024` as the active conda environment. On successful execution, it should print **'Package import test successful!'** without throwing any errors.
4. Make sure you can access the [Google document](https://docs.google.com/document/d/e/2PACX-1vSGK9QkaeX5pWgmxyiRyRm61Q1HOByW4Jx5a616NS_F-VbkdubsHkhyq_V2Oq-0HiT_OTVAKg8OY6UO/pub) containing the *"Announcements"* section. This document would be used for sharing the announcements during the exam.
5. Test the [submission](#submission) utility by submitting any 'ipynb' file using [the dry run submission form](https://forms.gle/bYxSEzTozsfLdQpe8). Opt for the "Send me a copy of my responses" option to receive an email confirmation of your submission. 

## Questions During the Exam

During the exam, we will use this [google doc](https://docs.google.com/document/d/e/2PACX-1vSGK9QkaeX5pWgmxyiRyRm61Q1HOByW4Jx5a616NS_F-VbkdubsHkhyq_V2Oq-0HiT_OTVAKg8OY6UO/pub) to post any clarifications or corrections to the questions(live updates). Please refer to this page regularly to see the latest updates.
To ensure efficiency and fairness, we will not reply to individual question directly. Instead, we will address common questions in this doc if they are relevant to a larger audience.  

*Note: For sharing documents with more than 100 viewers, Google recommends publishing them to the Web (details [here](https://support.google.com/a/users/answer/9308870?hl=en)). As a consequence, the document may no longer be updated in real-time by your Web browser. Thus, in order to view an up-to-date version of the document you might need to periodically refresh the page*


## High-level Guidelines and Rules

1. You cannot leave the room in the first and last 15 minutes.
2. Once seated, please turn off your mobile phones and place your phones and Camipro cards on the desk. 
3. You should be connected to the EPFL network for the duration of the exam and are not allowed to use VPNs or Hotspots.
4. You can use all the online resources you want, except for communication tools (emails, web chats, forums, phone, etc.) and AI-powered tools (e.g. ChatGPT, GitHub Copilot, LLMs, etc.) that have the potential to directly give you a solution. We will be monitoring the network for any unusual activity between 15:00 and 18:30.
5. You are allowed to use any built-in Python library that comes with Anaconda.
6.  You are allowed to use [Google Colab](https://colab.research.google.com/) or [EPFL Noto](https://noto.epfl.ch), however, it's your responsibility to ensure that the required Python packages (see the section [Conda environment](#Conda-environment) for details) are accessible in the execution environment and platform of choice.
7.  Don't forget to add a textual description of your thought process, the assumptions you made, and your results!
8.  Please write all your comments in English, and use meaningful variable names in your code.
9.  We suggest that you not obsess over small details in the beginning, and try to complete as many tasks as possible during the first 2 hours. Then, go back to the obtained results, write meaningful comments, and debug your code if you have found any glaring mistakes.
10. Fully read the instructions for each question before starting to solve it to avoid misunderstandings, and remember to save your notebook regularly.
11. We will **not run your notebook for you**! Rather, we will grade it as is, which means that only the results contained in your evaluated code cells will be considered, and we will not see the results in unevaluated code cells. Thus, be sure to hand in a **fully run and evaluated notebook**.
12. In continuation to the previous point, interactive plots, such as those generated using `plotly`, should be **strictly avoided**!
13. Remember, this is not a homework assignment -- no teamwork allowed! Any communication with others, including forum, chat, email, etc., is strictly forbidden.
14. You can use Stack Overflow but you are not allowed to post questions on it, just to read what is already there.
15. You can use lecture notes, lab notebooks and the internet to search for information (as long as you are not communicating with others or using AI-powered tools listed above).
