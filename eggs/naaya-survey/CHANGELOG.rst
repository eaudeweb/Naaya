1.3.18 (unreleased)
------------------

1.3.17 (2022-09-06)
------------------
* fix getting details of signups (Naaya Meeting)
  [valipod refs #154063]
* add possibility to deny editing own answers [valipod]

1.3.16 (2021-12-23)
------------------
* add explicit fieldset in main content with 'survey expired' message
  [valipod]
* hide 'Survey details' box if survey is expired and user is not admin
  [valipod]
* support zope root users sumitting answers
  [valipod]

1.3.15 (2021-12-22)
------------------
* decode user data from error messages, if needed [valipod]

1.3.14 (2021-12-21)
------------------
* fix translation for erorr messages containing user data [valipod]
* further css fixes [dumitval]

1.3.13 (2021-12-15)
------------------
* further css fixes [dumitval]

1.3.12 (2021-12-14)
------------------
* further css fixes [dumitval]

1.3.11 (2021-12-14)
------------------
* relax css in survey edit mode [dumitval]

1.3.10 (2020-04-13)
===================
* styling updates for Eionet 2020 style compatibility [dumitval]

1.3.9 (2019-11-18)
===================
* compatibility fix for Pluggable Auth Service [dumitval]

1.3.8 (2019-09-27)
===================
* changes for the Eionet NFP meeting automatic survey [dumitval]

1.3.7 (2017-01-20)
===================
* bugfix in survey answers export [dumitval]

1.3.6 (2016-11-18)
===================
* update file widget to use blob storage instead of extfile [dumitval]

1.3.5 (2016-11-07)
===================
* error message when respondent name is not submitted (answers on behalf
  of participants) [dumitval]

1.3.4 (2016-08-31)
===================
* trying to download invalid file types should not return an error since
  it's only bots who try this [dumitval]

1.3.3 (2016-07-26)
===================
* change the style to display list bullets in answer view [dumitval]

1.3.2 (2016-07-19)
===================
* increase the maximum default file upload size to 10MB [dumitval]
* increase the font size of the question title [dumitval]

1.3.1 (2016-01-28)
===================
* use cookie-jar in wkhtmltopdf to fix Unauthorized issue [dumitval]

1.3.0 (2016-01-20)
===================
* google charts legend and colours improvements [dumitval]
* updated pygooglecharts to version 0.4 + changes [dumitval]

1.2.56 (2016-01-20)
===================
* prevent wkhtmltopdf page break within table cell [dumitval]

1.2.55 (2016-01-19)
===================
* small improvement in widget listing for many columns [dumitval]

1.2.54 (2015-05-20)
===================
* added pdf export of reports `needs wkhtmltopdf on system` [dumitval]

1.2.53 (2015-02-26)
===================
* allow authentication in parent meeting object before viewing own
  answer [dumitval]

1.2.52 (2015-02-25)
===================
* send email with answers to signups (survey in meeting) [dumitval]

1.2.51 (2015-02-05)
===================
* Bug fix: compatibility with naaya.content.bfiles
  [tiberich]

1.2.50 (2015-01-08)
===================
* modify excel export of answers to show matrix lines as separate
  columns [dumitval]

1.2.49 (2014-07-09)
===================
* CSS exception for headings within the tooltips [dumitval]

1.2.48 (2014-05-23)
===================
* bugfix related to deletion of questions [dumitval]

1.2.47 (2014-02-10)
===================
* bugfix in survey index related to the possible inclusion in an eionet meeting [dumitval]

1.2.46 (2014-02-07)
===================
* allow instantiating of the Matrix widget with rows and columns [dumitval]

1.2.45 (2014-02-05)
===================
* bugfix (old answers were not overwritten) [dumitval]

1.2.44 (2013-01-22)
===================
* 17695 Add survey content from other languages when the current one has none

1.2.43 (2014-01-16)
===================
* fix several draft answers issue [dumitval]

1.2.42 (2014-01-15)
===================
* fixed a email template bug [dumitval]

1.2.41 (2014-01-15)
===================
* fixed a email template bug [dumitval]
* xlwt and xlrd added to Naaya as dependencies. No need to assert availability. [dumitval]

1.2.40 (2014-01-10)
===================
* customisations of the email templates [dumitval]

1.2.39 (2014-01-10)
===================
* remove anonymous from view reports permission [dumitval]

1.2.38 (2014-01-09)
===================
* Fix for survey reports with anonymous users [dumitval]

1.2.37 (2013-12-18)
===================
* Send notification to owner also for anonymous users + email formatting [dumitval] 

1.2.36 (2013-12-09)
===================
* added possibility to answer in a participant's name [dumitval]

1.2.35 (2013-09-26)
===================
* define a local messages_html (view permission issues) [dumitval]
* specify anonymous status in confirmation mail [dumitval]

1.2.34 (2013-08-30)
===================
* show signup respondent name from parent meeting, if applicable [dumitval]
* bugfix in anonymous aswering system [dumitval]

1.2.33 (2013-08-29)
===================
* allow auth. users to answer anonymously [dumitval]

1.2.32 (2013-07-26)
===================
* removed duplicated notification to maintainer [dumitval]

1.2.31 (2013-06-03)
===================
* label and text change for anonymous responder email [dumitval]

1.2.30 (2013-05-24)
===================
* now the contributor property is set [dumitval]
* skip messages_html when adding a survey [dumitval]

1.2.29 (2013-04-15)
===================
* added inherit_view_permission method [dumitval]

1.2.28 (2013-03-26)
===================
* bugifx in survey session [nituacor]

1.2.27 (2013-03-21)
===================
* redirect to the parent after answer submit ONLY IF IN MEETING [dumitval]
* small template improvements [dumitval]

1.2.26 (2013-02-28)
===================
* bugfix in combobox matrix widget [moregale]

1.2.25 (2013-01-09)
===================
* bugfix in answers export [dumitval]

1.2.24 (2012-12-07)
===================
* bugfix in sender_email getter [dumitval]

1.2.23 (2012-11-06)
===================
* bugfix: #9938; improper unauthorized error on rendering answer [simiamih]
* bugfix: #9933; CSS fix inside survey_common.css [soniaand]

1.2.22 (2012-10-03)
===================
* bugfix: #1000; fixed KeyError on rendering survey report [simiamih]

1.2.21 (2012-09-10)
===================
* redirect to the parent after answer submit [dumitval]

1.2.20 (2012-05-22)
===================
* Enhanced error messages for report generation [dumitval]

1.2.19 (2012-04-27)
===================
* bugfix: AttributeError: generate_csv [nituacor]

1.2.18 (2012-02-03)
===================
* bugfix: utf8 labels in graphs [simiamih]

1.2.17 (2012-01-31)
===================
* bugfix: missing i18n [nituacor]

1.2.16 (2012-01-13)
===================
* Added i18n id for translation of 'Type' [dumitval]
* removed .txt from manifest [dumitval]

1.2.15 (2012-01-06)
===================
* check_item_title is now item_has_title [simiamih]

1.2.14 (2012-01-06)
===================
* added can_be_seen for MegaSurvey [simiamih]

1.2.13 (2011-12-09)
===================
* TypeError: sequence expected, NoneType found [nituacor]

1.2.12 (2011-12-09)
===================
* TypeError: sequence expected, NoneType found [nituacor]

1.2.11 (2011-12-09)
===================
* fix MatrixWidget initial value [nituacor]

1.2.10 (2011-12-08)
===================
* fix multiple choice widget initial value [andredor]

1.2.9 (2011-11-14)
==================
* permission information update [andredor]

1.2.8 (2011-10-24)
==================
* use reCAPTCHA for add forms [andredor]
* remove show_captcha wrapper [andredor]

1.2.7 (2011-10-19)
==================
* bufgix: default value False for allow_multiple_answers #714 [simiamih]

1.2.6 (2011-10-18)
==================
* xlwt dependency, rel="nofollow" on export link [simiamih]
* Bugfix in RadioWidget.get_value
* Administrators can now edit answers in expired surveys

1.2.5 (2011-09-23)
==================
* Merge Products.NaayaSurvey and Products.NaayaWidgets into a single package
  named "naaya-survey"

1.2.2 (2011-04-28)
==================
* Last version where Products.NaayaSurvey and Products.NaayaWidgets were
  separate packages
