#-- start of make_header -----------------

#====================================
#  Document post_merge_rootmap
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

cmt_post_merge_rootmap_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_post_merge_rootmap_has_target_tag

tags      = $(tag),$(CMTEXTRATAGS),target_post_merge_rootmap

WorkArea_tag = $(tag)

#cmt_local_tagfile_post_merge_rootmap = $(WorkArea_tag)_post_merge_rootmap.make
cmt_local_tagfile_post_merge_rootmap = $(bin)$(WorkArea_tag)_post_merge_rootmap.make

else

tags      = $(tag),$(CMTEXTRATAGS)

WorkArea_tag = $(tag)

#cmt_local_tagfile_post_merge_rootmap = $(WorkArea_tag).make
cmt_local_tagfile_post_merge_rootmap = $(bin)$(WorkArea_tag).make

endif

include $(cmt_local_tagfile_post_merge_rootmap)
#-include $(cmt_local_tagfile_post_merge_rootmap)

ifdef cmt_post_merge_rootmap_has_target_tag

cmt_final_setup_post_merge_rootmap = $(bin)setup_post_merge_rootmap.make
cmt_dependencies_in_post_merge_rootmap = $(bin)dependencies_post_merge_rootmap.in
#cmt_final_setup_post_merge_rootmap = $(bin)WorkArea_post_merge_rootmapsetup.make
cmt_local_post_merge_rootmap_makefile = $(bin)post_merge_rootmap.make

else

cmt_final_setup_post_merge_rootmap = $(bin)setup.make
cmt_dependencies_in_post_merge_rootmap = $(bin)dependencies.in
#cmt_final_setup_post_merge_rootmap = $(bin)WorkAreasetup.make
cmt_local_post_merge_rootmap_makefile = $(bin)post_merge_rootmap.make

endif

#cmt_final_setup = $(bin)setup.make
#cmt_final_setup = $(bin)WorkAreasetup.make

#post_merge_rootmap :: ;

dirs ::
	@if test ! -r requirements ; then echo "No requirements file" ; fi; \
	  if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi

javadirs ::
	@if test ! -d $(javabin) ; then $(mkdir) -p $(javabin) ; fi

srcdirs ::
	@if test ! -d $(src) ; then $(mkdir) -p $(src) ; fi

help ::
	$(echo) 'post_merge_rootmap'

binobj = 
ifdef STRUCTURED_OUTPUT
binobj = post_merge_rootmap/
#post_merge_rootmap::
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
post_merge_rootmap_once = 1
endif

ifdef post_merge_rootmap_once

post_merge_rootmapactionstamp = $(bin)post_merge_rootmap.actionstamp
#post_merge_rootmapactionstamp = post_merge_rootmap.actionstamp

post_merge_rootmap :: $(post_merge_rootmapactionstamp)
	$(echo) "post_merge_rootmap ok"
#	@echo post_merge_rootmap ok

#$(post_merge_rootmapactionstamp) :: $(post_merge_rootmap_dependencies)
$(post_merge_rootmapactionstamp) ::
	$(silent) abuild-merge-rootmap.py
	$(silent) cat /dev/null > $(post_merge_rootmapactionstamp)
#	@echo ok > $(post_merge_rootmapactionstamp)

post_merge_rootmapclean ::
	$(cleanup_silent) /bin/rm -f $(post_merge_rootmapactionstamp)

else

#post_merge_rootmap :: $(post_merge_rootmap_dependencies)
post_merge_rootmap ::
	$(silent) abuild-merge-rootmap.py

endif

install ::
uninstall ::

#-- end of cmt_action_runner_header -----------------
#-- start of cleanup_header --------------

clean :: post_merge_rootmapclean ;
#	@cd .

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(post_merge_rootmap.make) $@: No rule for such target" >&2
else
.DEFAULT::
	$(error PEDANTIC: $@: No rule for such target)
endif

post_merge_rootmapclean ::
#-- end of cleanup_header ---------------
