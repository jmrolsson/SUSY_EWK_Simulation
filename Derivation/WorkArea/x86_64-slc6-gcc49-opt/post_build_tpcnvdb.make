#-- start of make_header -----------------

#====================================
#  Document post_build_tpcnvdb
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

cmt_post_build_tpcnvdb_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_post_build_tpcnvdb_has_target_tag

tags      = $(tag),$(CMTEXTRATAGS),target_post_build_tpcnvdb

WorkArea_tag = $(tag)

#cmt_local_tagfile_post_build_tpcnvdb = $(WorkArea_tag)_post_build_tpcnvdb.make
cmt_local_tagfile_post_build_tpcnvdb = $(bin)$(WorkArea_tag)_post_build_tpcnvdb.make

else

tags      = $(tag),$(CMTEXTRATAGS)

WorkArea_tag = $(tag)

#cmt_local_tagfile_post_build_tpcnvdb = $(WorkArea_tag).make
cmt_local_tagfile_post_build_tpcnvdb = $(bin)$(WorkArea_tag).make

endif

include $(cmt_local_tagfile_post_build_tpcnvdb)
#-include $(cmt_local_tagfile_post_build_tpcnvdb)

ifdef cmt_post_build_tpcnvdb_has_target_tag

cmt_final_setup_post_build_tpcnvdb = $(bin)setup_post_build_tpcnvdb.make
cmt_dependencies_in_post_build_tpcnvdb = $(bin)dependencies_post_build_tpcnvdb.in
#cmt_final_setup_post_build_tpcnvdb = $(bin)WorkArea_post_build_tpcnvdbsetup.make
cmt_local_post_build_tpcnvdb_makefile = $(bin)post_build_tpcnvdb.make

else

cmt_final_setup_post_build_tpcnvdb = $(bin)setup.make
cmt_dependencies_in_post_build_tpcnvdb = $(bin)dependencies.in
#cmt_final_setup_post_build_tpcnvdb = $(bin)WorkAreasetup.make
cmt_local_post_build_tpcnvdb_makefile = $(bin)post_build_tpcnvdb.make

endif

#cmt_final_setup = $(bin)setup.make
#cmt_final_setup = $(bin)WorkAreasetup.make

#post_build_tpcnvdb :: ;

dirs ::
	@if test ! -r requirements ; then echo "No requirements file" ; fi; \
	  if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi

javadirs ::
	@if test ! -d $(javabin) ; then $(mkdir) -p $(javabin) ; fi

srcdirs ::
	@if test ! -d $(src) ; then $(mkdir) -p $(src) ; fi

help ::
	$(echo) 'post_build_tpcnvdb'

binobj = 
ifdef STRUCTURED_OUTPUT
binobj = post_build_tpcnvdb/
#post_build_tpcnvdb::
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
post_build_tpcnvdb_once = 1
endif

ifdef post_build_tpcnvdb_once

post_build_tpcnvdbactionstamp = $(bin)post_build_tpcnvdb.actionstamp
#post_build_tpcnvdbactionstamp = post_build_tpcnvdb.actionstamp

post_build_tpcnvdb :: $(post_build_tpcnvdbactionstamp)
	$(echo) "post_build_tpcnvdb ok"
#	@echo post_build_tpcnvdb ok

#$(post_build_tpcnvdbactionstamp) :: $(post_build_tpcnvdb_dependencies)
$(post_build_tpcnvdbactionstamp) ::
	$(silent) abuild-merge-genconfdb.py
	$(silent) cat /dev/null > $(post_build_tpcnvdbactionstamp)
#	@echo ok > $(post_build_tpcnvdbactionstamp)

post_build_tpcnvdbclean ::
	$(cleanup_silent) /bin/rm -f $(post_build_tpcnvdbactionstamp)

else

#post_build_tpcnvdb :: $(post_build_tpcnvdb_dependencies)
post_build_tpcnvdb ::
	$(silent) abuild-merge-genconfdb.py

endif

install ::
uninstall ::

#-- end of cmt_action_runner_header -----------------
#-- start of cleanup_header --------------

clean :: post_build_tpcnvdbclean ;
#	@cd .

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(post_build_tpcnvdb.make) $@: No rule for such target" >&2
else
.DEFAULT::
	$(error PEDANTIC: $@: No rule for such target)
endif

post_build_tpcnvdbclean ::
#-- end of cleanup_header ---------------
