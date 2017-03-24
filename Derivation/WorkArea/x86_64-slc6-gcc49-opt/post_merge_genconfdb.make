#-- start of make_header -----------------

#====================================
#  Document post_merge_genconfdb
#
#   Generated Tue Mar 21 22:19:19 2017  by jolsson
#
#====================================

include ${CMTROOT}/src/Makefile.core

ifdef tag
CMTEXTRATAGS = $(tag)
else
tag       = $(CMTCONFIG)
endif

cmt_post_merge_genconfdb_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_post_merge_genconfdb_has_target_tag

tags      = $(tag),$(CMTEXTRATAGS),target_post_merge_genconfdb

WorkArea_tag = $(tag)

#cmt_local_tagfile_post_merge_genconfdb = $(WorkArea_tag)_post_merge_genconfdb.make
cmt_local_tagfile_post_merge_genconfdb = $(bin)$(WorkArea_tag)_post_merge_genconfdb.make

else

tags      = $(tag),$(CMTEXTRATAGS)

WorkArea_tag = $(tag)

#cmt_local_tagfile_post_merge_genconfdb = $(WorkArea_tag).make
cmt_local_tagfile_post_merge_genconfdb = $(bin)$(WorkArea_tag).make

endif

include $(cmt_local_tagfile_post_merge_genconfdb)
#-include $(cmt_local_tagfile_post_merge_genconfdb)

ifdef cmt_post_merge_genconfdb_has_target_tag

cmt_final_setup_post_merge_genconfdb = $(bin)setup_post_merge_genconfdb.make
cmt_dependencies_in_post_merge_genconfdb = $(bin)dependencies_post_merge_genconfdb.in
#cmt_final_setup_post_merge_genconfdb = $(bin)WorkArea_post_merge_genconfdbsetup.make
cmt_local_post_merge_genconfdb_makefile = $(bin)post_merge_genconfdb.make

else

cmt_final_setup_post_merge_genconfdb = $(bin)setup.make
cmt_dependencies_in_post_merge_genconfdb = $(bin)dependencies.in
#cmt_final_setup_post_merge_genconfdb = $(bin)WorkAreasetup.make
cmt_local_post_merge_genconfdb_makefile = $(bin)post_merge_genconfdb.make

endif

#cmt_final_setup = $(bin)setup.make
#cmt_final_setup = $(bin)WorkAreasetup.make

#post_merge_genconfdb :: ;

dirs ::
	@if test ! -r requirements ; then echo "No requirements file" ; fi; \
	  if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi

javadirs ::
	@if test ! -d $(javabin) ; then $(mkdir) -p $(javabin) ; fi

srcdirs ::
	@if test ! -d $(src) ; then $(mkdir) -p $(src) ; fi

help ::
	$(echo) 'post_merge_genconfdb'

binobj = 
ifdef STRUCTURED_OUTPUT
binobj = post_merge_genconfdb/
#post_merge_genconfdb::
#	@if test ! -d $(bin)$(binobj) ; then $(mkdir) -p $(bin)$(binobj) ; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)$(binobj)
endif

${CMTROOT}/src/Makefile.core : ;
ifdef use_requirements
$(use_requirements) : ;
endif

#-- end of make_header ------------------
#-- start of cmt_action_runner_header ---------------

ifdef ONCE
post_merge_genconfdb_once = 1
endif

ifdef post_merge_genconfdb_once

post_merge_genconfdbactionstamp = $(bin)post_merge_genconfdb.actionstamp
#post_merge_genconfdbactionstamp = post_merge_genconfdb.actionstamp

post_merge_genconfdb :: $(post_merge_genconfdbactionstamp)
	$(echo) "post_merge_genconfdb ok"
#	@echo post_merge_genconfdb ok

#$(post_merge_genconfdbactionstamp) :: $(post_merge_genconfdb_dependencies)
$(post_merge_genconfdbactionstamp) ::
	$(silent) abuild-merge-genconfdb.py
	$(silent) cat /dev/null > $(post_merge_genconfdbactionstamp)
#	@echo ok > $(post_merge_genconfdbactionstamp)

post_merge_genconfdbclean ::
	$(cleanup_silent) /bin/rm -f $(post_merge_genconfdbactionstamp)

else

#post_merge_genconfdb :: $(post_merge_genconfdb_dependencies)
post_merge_genconfdb ::
	$(silent) abuild-merge-genconfdb.py

endif

install ::
uninstall ::

#-- end of cmt_action_runner_header -----------------
#-- start of cleanup_header --------------

clean :: post_merge_genconfdbclean ;
#	@cd .

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(post_merge_genconfdb.make) $@: No rule for such target" >&2
else
.DEFAULT::
	$(error PEDANTIC: $@: No rule for such target)
endif

post_merge_genconfdbclean ::
#-- end of cleanup_header ---------------
