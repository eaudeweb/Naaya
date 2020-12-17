1.5.8 (unreleased)
-----------------
* allow skipping sections that are marked as header [dumitval]

1.5.7 (2020-11-20)
-----------------
* redirect to consultation index after successfully authenticating
  as invitee [dumitval]

1.5.6 (2020-02-21)
-----------------
* merge style improvements from different IGs [dumitval]

1.5.5 (2019-09-27)
-----------------
* open hyperlinks from talkback comments in new window [dumitval]

1.5.4 (2019-09-13)
-----------------
* add permission to manage comments, separated from admin [dumitval]

1.5.3 (2019-03-01)
-----------------
* improve styling for the comment box [dumitval]

1.5.2 (2019-02-20)
-----------------
* fix for the comments count for invited commenters [dumitval]

1.5.1 (2019-01-24)
------------------
* fixing update script [batradav]

1.5.0 (2019-01-24)
------------------
* adding extra fields for anonymous contributors
  - email
  - organisation
* replacing comment.contributor (str) with Contributor namedtuple
* replacing get_contributor_name with get_contributor_info
* removing contributor_name attribute, same value is available at runtime
  through get_contributor_info()['display_name']
* adding update script for existing consultations
* improving the commenting form and pop-up
  - moving error messages to bottom so they're more visible
  - centered the pop-up window
[batradav]

1.4.49 (2018-06-28)
-------------------
* handle UnicodeEncodeError in xlwt in formulas [dumitval]

1.4.48 (2018-05-07)
-------------------
* add hyperlink to user profile in comments export [dumitval]

1.4.47 (2018-02-27)
-------------------
* improvement for section formatting in talkback index [dumitval]
* corrected security declaration [dumitval]

1.4.46 (2016-09-15)
-------------------
* add permission to comment after deadline to permission administration
  [dumitval]
* wording change in invitation email [dumitval]
* added support for the verbose edw version of validate_email [dumitval]
* fullscreen to apply to section index, too [dumitval]

1.4.45 (2016-02-17)
-------------------
* bugfix in allowing Reviewers to invite [dumitval]

1.4.44 (2015-11-03)
-------------------
* check and correct paragraph_list for consistency [dumitval]
* add a 'delete paragraph' button on section edit [dumitval]

1.4.43 (2015-10-22)
-------------------
* set initial permissions on install + update script [dumitval]

1.4.42 (2015-10-14)
-------------------
* consultations index customisations based on ampconsultation IG [dumitval]
* removed disabled@eionet.europa.eu as filter for users
  (disabled users are already filtered out) [dumitval]

1.4.41 (2015-06-25)
-------------------
* make email subject mandatory (needed for email archive listing) [dumitval]

1.4.40 (2015-06-25)
-------------------
* added CC to email sender [dumitval]

1.4.39 (2015-05-28)
-------------------
* select Eionet users to insert in email recipients [dumitval]

1.4.38 (2015-05-20)
-------------------
* bugfix related to allow reviewer to invite [dumitval]

1.4.37 (2015-04-23)
-------------------
* bugfix on talkback edit page (role assignment) [dumitval]

1.4.36 (2015-03-03)
-------------------
* allow 1024 characters is a excel cell (export) [dumitval]

1.4.35 (2014-12-02)
-------------------
* Add files to consultation [dumitval]

1.4.34 (2014-08-21)
-------------------
* Bug fix: make a red message when previewing a file about needing to reupload file
  [tiberich #20725]

1.4.33 (2014-07-28)
-------------------
* Send emails from within the consultation, save them in archive [dumitval]

1.4.32 (2014-04-07)
-------------------
* Task #17799 - choose emails to export to xcel [baragdan]
* fixed xcel typo [dumitval]

1.4.31 (2014-01-17)
-------------------
* hide "Reply" button if the user doesn't have commenting rights [dumitval]
* xlwt and xlrd added to Naaya as dependencies. No need to assert availability. [dumitval]

1.4.30 (2014-01-07)
-------------------
* task 17799 - export mail list to xcel [baragdan]

1.4.29 (2013-12-18)
-------------------
class-based selection of cells with emails to be validated [dumitval]

1.4.28 (2013-12-11)
-------------------
* Email Validation - resolve validation in backend threads (avoid server load) [baragdan]

1.4.27 (2013-12-10)
-------------------
* added option to skip paragraph splitting [dumitval]

1.4.26 (2013-12-09)
-------------------
* Email Validation - controll js parallelism (avoid server load) [baragdan]

1.4.25 (2013-12-05)
-------------------
* Added email validation [baragdan]

1.4.24 (2013-11-19)
-------------------
* archive sent invitation mails + listing and individual view [dumitval]
* testfix admin_comments [dumitval]

1.4.23 (2013-11-04)
-------------------
* added export of own comments for normal users [dumitval]

1.4.22 (2013-07-26)
-------------------
* removed duplicated notification to maintainer [dumitval]

1.4.21 (2013-02-27)
-------------------
* #4595 - send invitation on behalf of
1.4.20 (2012-12-11)
-------------------
* comments are no longer subject of approval [simiamih]

1.4.19 (2012-11-28)
-------------------
* bugfix: #10085: removed misleading prompt when leaving comments [mihaitab]

1.4.18 (2012-11-22)
-------------------
* backwards compatibility: simplejson as json [mihaitab]

1.4.17 (2012-11-20)
-------------------
* (#10022) Improve comments summary. Add comments trend chart [mihaitab]

1.4.16 (2012-11-20)
-------------------
* (#10022) Improve comments summary [mihaitab]

1.4.15 (2012-11-20)
-------------------
* bugfix: #10002; write Byte Order Marker for the exported CSV [nituacor]

1.4.14 (2012-11-20)
-------------------
* ugly temporary quickfix for flickering scrollbar of iframe [simiamih]
* add "replies" column to comments tables [moregale]

1.4.13 (2012-08-16)
-------------------
* Added permission to comment/reply after consultation deadline [dumitval]

1.4.12 (2012-08-08)
-------------------
* bugfix: close comment window link for anonymous [simiamih]

1.4.11 (2012-07-13)
-------------------
* #964 - redesigned comment edit/delete permissions [simiamih]

1.4.10 (2012-07-04)
-------------------
* adapted to correctly create footnote links [dumitval]
* fixed deprecation warning (bad super addressing) [simiamih]
* fixed tests: invitees comments do not need aproval [simiamih]

1.4.9 (2012-03-23)
------------------
* Removed approval workflow for comments [dumitval]

1.4.8 (2012-03-14)
------------------
* feature: bulk send invitations [simiamih]
* fixed permission for "Manage comments" button [simiamih]

1.4.7 (2012-02-21)
------------------
* Added confirmation dialog when closing an unsubmitted comment window [dumitval]

1.4.6 (2012-01-19)
------------------
* bugfix: iframe resize in IE9 [simiamih]

1.4.5 (2012-01-06)
------------------
* Bugfix for editing a comment [dumitval]

1.4.4 (2011-11-14)
------------------
* permission information update [andredor]

1.4.3 (2011-11-04)
------------------
* update script for consultations without invitations [andredor]
