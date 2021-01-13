1.4.66 (unreleased)
-------------------

1.4.65 (2021-01-13)
-------------------
* update nfp_nrc location to eionet.europa.eu [dumitval]
* add interface for IEnvcoord site [dumitval]
* remove hard dependency to eea.usersdb [dumitval]

1.4.64 (2020-12-18)
-------------------
* fix select height in the 2020 layout + update script [dumitval]

1.4.63 (2020-06-17)
-------------------
* customize site_admin_users to hide local users [dumitval]

1.4.62 (2020-05-26)
-------------------
* add extranet_reporters link getter [dumitval]

1.4.61 (2020-05-20)
-------------------
* standard template logo url improvements [dumitval]

1.4.60 (2020-04-13)
-------------------
* introduce eionet_2020 layout [dumitval]

1.4.59 (2019-11-18)
-------------------
* request_ig_access fix related to the Pluggable Auth Service [dumitval]

1.4.58 (2019-11-12)
-------------------
* profile_overview fix related to the Pluggable Auth Service [dumitval]

1.4.57 (2019-11-07)
-------------------
* added compatibility with Pluggable Auth Service as root acl [dumitval]
* update script for standard template to display name of singups in
  talkback and meetings [dumitval]

1.4.56 (2019-10-31)
-------------------
* changes in the display of disabled users [dumitval]

1.4.55 (2019-10-14)
-------------------
* changes in the default left portlets + update script [dumitval]

1.4.54 (2019-09-05)
-------------------
* remove any WebEx-related functionality [dumitval]
* bugfix in member_search related to the "Former Eionet member" message
  [dumitval]

1.4.53 (2019-04-02)
-------------------
* fix Size limit exceeded in member_search_html [dumitval]

1.4.52 (2019-03-04)
-------------------
* get_external_user_info: handle users without the disabled property [dumitval]

1.4.51 (2019-03-01)
-------------------
* display 'Former eionet member' for deactivated users in IG member_search
  [dumitval]

1.4.50 (2018-12-27)
-------------------
* remove google analytics [dumitval]

1.4.49 (2018-06-14)
-------------------
* fix for inside_meeting method crashing [dumitval]

1.4.48 (2018-03-19)
-------------------
* improvements in displaying info about disabled users [dumitval]

1.4.47 (2018-03-15)
-------------------
* no link to user profile for disabled users
* display generic user name for disabled users (when displaying owner
  info)
* google analytics IP anonymisation refs #87835 [dumitval]

1.4.46 (2017-04-13)
-------------------
* updated ajax call to archives to https and several other http links [dumitval]

1.4.45 (2017-04-10)
-------------------
* Bug fix: forum-test eionet is not responding
  - fixed reverse changes
  [chiridra #84148]

1.4.44 (2017-04-07)
-------------------
* updated some links to www.eionet.europa.eu to https [dumitval]
* Bug fix: LDAP dump causes large spikes in load
  - revert changes
  [chiridra #80233]

1.4.43 (2017-04-03)
-------------------
* Bug fix: LDAP dump causes large spikes in load
  - removed ldap_cache reference and refactor the code
  [chiridra #80233]

1.4.42 (2016-11-11)
-------------------
* get notify_on_errors_email from buildout [dumitval]

1.4.41 (2016-10-07)
-------------------
* wording change for NFP Reportnet members edit link [dumitval]

1.4.40 (2016-10-03)
-------------------
* added NFP AWP roles administration link [dumitval]
* added some error handling in index_html [dumitval]

1.4.39 (2016-04-11)
-------------------
* root index fix for IGs without welcome text property [dumitval]

1.4.38 (2016-04-04)
-------------------
* fix sending notification email after role request approval [dumitval]

1.4.37 (2016-01-22)
-------------------
* compatibility update in group_member_search [dumitval]
* fix for a crash with latin1 username [dumitval]

1.4.36 (2015-10-26)
-------------------
* typo fix in skel.xml [dumitval]

1.4.35 (2015-10-26)
-------------------
* updated skel permissions for use in reset role [dumitval]

1.4.34 (2015-04-28)
-------------------
* configured jstree in meeting to allow selecting inside of the meeting
  itself [dumitval]

1.4.33 (2015-01-27)
-------------------
* Bug fix: avoid error on HEAD request on <application>/@@index.html
  [tiberich #10124]

1.4.32 (2015-01-12)
-------------------
* Bug fix: avoid navigation portlet spilling errors when user is anonymous
  [tiberich]

1.4.31 (2014-10-31)
-------------------
* Bug fix: fix label for member search access level column
  [tiberich 21517]

1.4.30 (2014-10-27)
-------------------
* filter IGs on forum, projects and archives homepage [dumitval]

1.4.29 (2014-10-17)
-------------------
* Bug fix: allow admins_only query parameter to make the member search linkable
  when just the admins should be shown on the initial page
  [tiberich #4505]

1.4.28 (unreleased)
-------------------
* modified some tests where the old "Leader" term was used [dumitval]

1.4.27 (2014-08-27)
-------------------
* Change: renamed create new member option in navigation portlet menu
  [tiberich #20187]

1.4.26 (2014-08-25)
-------------------
* In the navigation portlet, added create user link for NFPs

1.4.25 (2014-08-01)
-------------------
* fix username encoding in request_access emails [dumitval]

1.4.24 (2014-07-30)
-------------------
* Bug fix: show role id in profile overview page
  [tiberich #20522]

1.4.23 (2014-07-03)
-------------------
* added a link to the how to video on nfp-eionet [dumitval]

1.4.22 (2014-06-30)
-------------------
* update script to correct possible duplicated links to the WebEx mail
  feature [dumitval]
* Replaced "Group leader" by "Group administrator" wherever this
  appeared [dumitval]

1.4.21 (2014-04-23)
-------------------
* handle users without email addresses [dumitval]

1.4.20 (2014-04-10)
-------------------
* bugfix in the update script [dumitval]

1.4.19 (2014-04-10)
-------------------
* Changed update script for login/logout to redirect to member search [dumitval]

1.4.18 (2014-04-09)
-------------------
* fix to show also users with several roles in member search [dumitval]

1.4.17 (2014-04-09)
-------------------
* added a "Show all administrators" button on the member search [dumitval]

1.4.16 (2014-03-10)
-------------------
* `update` "Request WebEx permission" added to contributors [dumitval]

1.4.15 (2014-03-05)
-------------------
* display comments for older file versions with a fainter colour [dumitval]
* change permission for the WebEx meeting link in skel [dumitval]

1.4.14 (2014-03-03)
-------------------
* `update script` for changing permission on the WebEx planing link [dumitval]

1.4.13 (2014-02-21)
-------------------
* refactored profile_overview ajax code for Chrome compatibility [dumitval]

1.4.12 (2014-02-18)
-------------------
* style improvement for the administrative notification (black on yellow) [dumitval]
* Check access and subscriptions one ig at a time [dumitval]

1.4.11 (2014-02-04)
-------------------
* Show only "Meeting observer" in role request page if request came from
  a meeting object [dumitval]

1.4.10 (2014-01-31)
-------------------
* fix the folder listing (colspan =2) [dumitval]

1.4.9 (2014-01-31)
-------------------
* Add option to request "Meeting Observer" role [dumitval]
* Show the 'Limited access' information in a separate column [dumitval]

1.4.8 (2014-01-14)
-------------------
* `update` changed logout link to directly logout [dumitval]

1.4.7 (2013-10-10)
-------------------
* added link to nfp organisations [dumitval]

1.4.6 (2013-07-26)
-------------------
* updated default permissions [simiamih]

1.4.5 (2013-07-10)
-------------------
* linked icon-sized photo to the main photo using lightbox [dumitval]

1.4.4 (2013-07-10)
-------------------
* added user pictures in folder listing (if available) [dumitval]
* deleted getMaintainersEmails override [dumitval]

1.4.3 (2013-07-10)
-------------------
* identify user source after lowering case [dumitval]

1.4.2 (2013-07-10)
-------------------
* links to eionet user profiles from folder listing [dumitval]

1.4.1 (2013-07-01)
-------------------
* #9607; Eionet full profile client implementation [simiamih]

1.3.14 (2013-06-11)
-------------------
* #4525 archives' index page [simiamih]

1.3.13 (2013-05-24)
-------------------
* moved update script to Naaya Core [dumitval]
* fixed rel path in std template [simiamih]

1.3.12 (2013-05-23)
-------------------
* #14601 update script to give skip captcha to Authenticated [dumitval]

1.3.11 (2013-05-22)
-------------------
* refs: #14214; improvements to webex meeting request [mihaitab]
* remove contact webex form from Email settings page [mihaitab]
* #14545 override getMaintainersEmails() from NySite [mihaitab]

1.3.10 (2013-05-20)
-------------------
* template fix [dumitval]

1.3.9 (2013-05-20)
-------------------
* support for reCAPTCHA keys from buildout [dumitval]

1.3.8 (2013-05-17)
-------------------
* auto-create meeting in webex request, improvements [mihaitab]

1.3.7 (2013-05-08)
-------------------
* moved help to a separate package [dumitval]

1.3.6 (2013-05-02)
-------------------
* moved help files to disk [dumitval]

1.3.5 (2013-04-26)
-------------------
* bugfix in meeting pointer custom templates [dumitval]

1.3.4 (2013-03-29)
-------------------
* bugfixes, refactorting WebEx planning email [mihaitab]
* Adding the WebEx planning email *update* [nituacor]

1.3.3 (2013-03-26)
-------------------
* Update Meeting pointer widgets *update* [nituacor]
* View for Reviewer [simiamih]

1.3.2 (2013-03-04)
-------------------
* update gw_common_css to Naaya Disk File *update* [mihaitab]
* migrate gw_common_css from naaya style to Naaya Disk file [mihaitab]

1.3.1 (2013-02-25)
-------------------
* updated common.css [bulanmir]
* updated link to nfp_nrc tool [simiamih]

1.3.0 (2013-02-08)
-------------------
* changed index headers, groupedIGs can be removed in ZODB [simiamih]

1.2.22 (2013-01-31)
-------------------
* #10266 - Rename button changed [mihaitab]

1.2.21 (2012-12-18)
-------------------
* Alert on 'Delete Folder' if existing checked items inside [mihaitab]

1.2.20 (2012-12-13)
-------------------
* Link to the bulk mail administration [dumitval]
* logged granted access requests [mihaitab]

1.2.19 (2012-11-23)
-------------------
* fixed session buffering: one can review a request only once [mihaitab]
* added meaningful error message on reviewing request access [mihaitab]
* revised email texts #4600 [simiamih]
* tests bugfix: test_profileclient.InterestGroupsTestCase [nituacor]
* improve style for Request access page [soniaand]

1.2.18 (2012-11-09)
-------------------
* redesigned access request and review access request [simiamih]
* update Owner edit permissions *update* [nituacor]

1.2.17 (2012-10-09)
-------------------
* include IG Logger in admin menu [simiamih]

1.2.16 (2012-10-05)
-------------------
* default talkback permissions by skel setting [simiamih]
* bugfix: cut/copy buttons were not working anymore [simiamih]

1.2.15 (2012-10-03)
-------------------
* Naaya Mega Survey content-type enabled by default [simiamih]
* naaya-delete-modal for both Delete and Delete Folder [simiamih]
* Removed float for 'Tips' on login form [bogdatan]

1.2.14 (2012-07-03)
-------------------
* using network_name in default index for groupware [simiamih]
* Reverted a change in site_admin_properties [dumitval]

1.2.13 (2012-07-02)
-------------------
* bugfix: *update* for folders with wrong releasedate [bogdatan]

1.2.12 (2012-06-29)
-------------------
* Added site_admin_template to skel (temporary) [dumitval]
* All Naaya Skins and images removed before skel loading [dumitval]
* DiskFile allow_path to layout schemes [dumitval]

1.2.11 (2012-06-25)
-------------------
* changed to use http_proxy from buildout [dumitval]
* External link for recaptcha [dumitval]

1.2.10 (2012-06-07)
-------------------
* eionet forum index uses text settings for messages [simiamih]
* #885 - using 3 level cutoff for subscriptions in profile_overview [simiamih]
* improved headings in profile overview [bogdatan]

1.2.9 (2012-06-06)
------------------
* Improved profile overview to show only the IGs that account is
  explicitly assigned [bogdatan]

1.2.8 (2012-05-23)
------------------
* using port when connecting to ldap in member_search [simiamih]
* fixed test for profileoverview [simiamih]

1.2.7 (2012-05-22)
------------------
* custom interface for SINAnet instance [simiamih]
* profileoverview: also use port when creating ldap connection [simiamih]

1.2.6 (2012-05-15)
------------------
* explanatory text for ig membership request [dumitval]

1.2.5 (2012-05-14)
-------------------
* member_search now searches in both uid and full name [dumitval]

1.2.4 (2012-05-10)
-------------------
* refactored profile overview, subscriptions on callback [simiamih]

1.2.3 (2012-05-04)
-------------------
* using ny_ldap_group_roles meta in catalog *update* [simiamih]

1.2.2 (2012-04-27)
-------------------
* bugfix: AttributeError: generate_csv [nituacor]

1.2.1 (2012-04-17)
-------------------
* delete button for nyfolders [simiamih]

1.2.0 (2012-04-13)
-------------------
* Created a JSON view to return all portals from
  archives.eionet.europa.eu for forum.eionet.europa.eu [bogdatan]

1.1.22 (2012-04-12)
-------------------
* customizable instance titles and welcome text [simiamih]

1.1.21 (2012-04-10)
-------------------
* Fixed NFP Admin Link to be called only for nfp-eionet website [bogdatan]
* Fixed profile overview to get local roles for specified user [bogdatan]

1.1.20 (2012-04-04)
-------------------
* Changed from search.eionet.europa.eu/search.jsp to Google Search [bogdatan]
* Updated administration portlet with comments management section
  and API keys status section [bogdatan]

1.1.19 (2012-03-16)
-------------------
* fixed zope 2.12 merging GET and POST in review_ig_request [simiamih]
* fixed tests: index_html is now simpleView [simiamih]

1.1.18 (2012-03-15)
-------------------
* added nofollow to zip download links [dumitval]

1.1.17 (2012-02-23)
-------------------
* fixed js for IE - profileoverview [bogdatan]

1.1.16 (2012-02-22)
-------------------
* fixed sorted NameError in profileoverview index.pt [simiamih]

1.1.15 (2012-02-22)
-------------------
* nfp_nrc link is enabled in nfp-eionet [simiamih]

1.1.14 (2012-02-15)
-------------------
* using ldap cache to display all members in members search [bogdatan]

1.1.13 (2012-02-10)
-------------------
* profileoverview shows specific profile by GET for managers [bogdatan]

1.1.12 (2012-02-02)
-------------------
* updated zope_customs documentation

1.1.11 (2012-02-02)
-------------------
* changed from customized index page to simpleView [bogdatan]
* changed names in IGs listing [bogdatan]
* archived IGs list made collapsible [bogdatan]
* added 'Edit NRC members' for nfp-eionet, currently disabled
  from py until CIRCA migration [bogdatan]
* profileoverview shows local roles owned by belonging to
  a ldap group [simiamih]
* profileoverview - ajax loading ig roles + role names [simiamih]
* list all button in member search

1.1.10 (2012-01-18)
-------------------
* bugfix: decode user names used in email template [simiamih]

1.1.9 (2012-01-16)
------------------
* Added modification time to the folder listing [dumitval]

1.1.8 (2012-01-13)
------------------
* Added i18n id for translation of 'Type' [dumitval]

1.1.7 (2012-01-12)
------------------
* fix style and logos for left/right logos [simiamih]

1.1.6 (2012-01-12)
------------------
* Fix name of Groupware bundle [dumitval]

1.1.5 (2012-01-11)
------------------
* updated common styles [bulanmir]

1.1.4 (2012-01-09)
------------------
* load groupware bundle [dumitval]
* changed message on member search page [dumitval]
* filter display for User management search [andredor]
* feature: naaya.groupware.profileoverview [simiamih]

1.1.3 (2011-10-28)
------------------
* Owner can have just edit content permission (admin other properties) [andredor]
* standard templates updated to site logo changes [dumitval]

1.1.2 (2011-10-14)
------------------
* portlet administration on disk for new gw sites [andredor]
* portlet administration also on disk [andredor]
* IGWSite interface (derived from INySite) [andredor]
