1.4.28 (unreleased)
--------------------
* support exporting to zip from console script (without REQUEST)
  [valipod]

1.4.27 (2020-03-27)
--------------------
* compatibility with destinet [dumitval]

1.4.26 (2019-07-09)
--------------------
* backwards compatibility on download link [dumitval]

1.4.25 (2016-11-18)
--------------------
* update script for naaya survey file widgets [dumitval]

1.4.24 (2016-05-30)
--------------------
* switch to datetime.now for last modification (i.e. CET) [dumitval]

1.4.23 (2015-10-06)
--------------------
* show file in other language if the current language has no version [dumitval]

1.4.22 (2015-07-07)
--------------------
* Feature: show commited blob path in a NyBlobFile's __repr__
  [tiberich]

1.4.21 (2015-03-27)
--------------------
* display a meaningful error message when the file could not be created
  (title or id issues) [dumitval]

1.4.20 (2015-02-26)
--------------------
* get last upload date for site_search [dumitval]

1.4.19 (2015-02-09)
--------------------
* Feature: added a view to report on all objects in the database with a reference
  to an ExtFile
  [tiberich #3929]

1.4.18 (2015-01-5)
--------------------
* Bug fix: also migrate Naaya Survey Answer as they can have attachments
  [tiberich #3929]

1.4.17 (2014-11-25)
--------------------
* Bug fix: always seek to 0 the streams that when constructing a bfile
  [tiberich #3929]

1.4.16 (2014-11-25)
--------------------
* Bug fix: fixes migration of Naaya File with bfile storage to Naaya Blob File
  [tiberich #3929]

1.4.15 (2014-11-25)
--------------------
* Bug fix: fixes migration of Naaya File with bfile storage to Naaya Blob File
  [tiberich #3929]

1.4.14 (2014-11-24)
--------------------
* Feature: added migration of extfiles storage for NyPublication
  [tiberich #3929]

1.4.13 (2014-11-21)
--------------------
* Bug fix: don't fail on migration of already migrated ext files/ ny files
  [tiberich #3929]

1.4.12 (2014-11-19)
--------------------
* improvements to the migrations [tiberich]

1.4.11 (2014-11-18)
--------------------
* Bug fix: upload blobs in old _versions storage on migration, to avoid assigning them
  a language
  [tiberich #3929]

1.4.10 (2014-11-14)
--------------------
* Feature: merge code from naaya.content.localizedbfile. Now all bfiles are localized
  [tiberich #3929]

1.4.9 (2014-11-03)
--------------------
* Bug fix: don't skip migration of talkback comments because of missing extfile
  [tiberich #3929]
* Bug fix: raise NotFound when the download page is retrieved for a BFile without 
  any uploaded content
  [tiberich #3929]

1.4.8 (2014-10-29)
--------------------
* Bug fix: skip files from being migrated if their extfile is broken
  [tiberich #3929]

1.4.7 (2014-10-29)
--------------------
* Bug fix: issue warnings when extfile is broken
  [tiberich #3929]

1.4.6 (2014-10-29)
--------------------
* PEP8 code formatting in some files [dumitval]
* strip leading underscores from new filenames [dumitval]
* Bug fix: added migration for naaya.content.talkback comment attachments
  [tiberich #3929]
* Bug fix: added migration for naaya survey attachment files
  [tiberich #3929]

1.4.5 (2014-10-24)
--------------------
* strip leading underscores from the filename in download url [dumitval]

1.4.4 (2014-10-10)
--------------------
* added an error handling on update script NyFile2NyBlob [dumitval]

1.4.3 (2014-10-10)
--------------------
* improve update scripts for migration from NyFile and NyExtFile to Blob
  [tiberich

1.4.2 (2014-10-10)
--------------------
* `update` execute the 'PhotoArchive and MediaFiles: Migrate ExtFiles to Blobs'
  migration to properly migrate the photoarchive  and media files to blob
  storage [tiberich #3929]

1.4.1 (2014-10-10)
--------------------
* improve extfile to bfile update scripts to delete original files [dumitval]

1.4.0 (2014-10-09)
--------------------
* Merge with the no-extfile branch
  [tiberich #3929]

1.3.14 (2014-04-04)
--------------------
* bugfix related to comments to removed versions [dumitval]
* bugfix related to incorrect timezone conversion [dumitval]

1.3.13 (2014-03-05)
--------------------
* Allow pairing of comments with document versions [dumitval]

1.3.12 (2013-07-10)
--------------------
* link to the contributor profile from the index page [dumitval]

1.3.11 (2013-05-17)
--------------------
* #4547 comment#9; bfile_index tpl small changes in labels [simiamih]

1.3.10 (2013-02-22)
--------------------
* newest versions first [simiamih]

1.3.9 (2012-12-19)
------------------
* #10213 - eliminate redundant notifications sent by zip upload [mihaitab]
* opening file index page is not a view event [simiamih]

1.3.8 (2012-10-09)
------------------
* view/download events are triggered [simiamih]

1.3.7 (2012-10-04)
------------------
* revert ensure_tzinfo removal [simiamih]

1.3.6 (2012-10-04)
------------------
* version timestamps are saved with tzinfo [simiamih]
* Added 'Uploaded by' column in versions table [bogdatan]

1.3.5 (2012-07-18)
------------------
* Added contributor to versions [bogdatan]
* check_item_title is now item_has_title [simiamih]
* fixed adapter to work with localizedbfile [simiamih]

1.3.4 (2012-01-13)
------------------
* Added i18n id for translation of 'Type' [dumitval]

1.3.3 (2011-11-17)
------------------
* portal_map methods are no longer called if the content type is not
  geo_enabled [dumitval]

1.3.2 (2011-11-14)
------------------
* permission information update [andredor]
