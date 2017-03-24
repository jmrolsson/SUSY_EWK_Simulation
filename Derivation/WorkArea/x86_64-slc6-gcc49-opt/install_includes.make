#-- start of make_header -----------------

#====================================
#  Document install_includes
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

cmt_install_includes_has_no_target_tag = 1

#--------------------------------------------------------

ifdef cmt_install_includes_has_target_tag

tags      = $(tag),$(CMTEXTRATAGS),target_install_includes

WorkArea_tag = $(tag)

#cmt_local_tagfile_install_includes = $(WorkArea_tag)_install_includes.make
cmt_local_tagfile_install_includes = $(bin)$(WorkArea_tag)_install_includes.make

else

tags      = $(tag),$(CMTEXTRATAGS)

WorkArea_tag = $(tag)

#cmt_local_tagfile_install_includes = $(WorkArea_tag).make
cmt_local_tagfile_install_includes = $(bin)$(WorkArea_tag).make

endif

include $(cmt_local_tagfile_install_includes)
#-include $(cmt_local_tagfile_install_includes)

ifdef cmt_install_includes_has_target_tag

cmt_final_setup_install_includes = $(bin)setup_install_includes.make
cmt_dependencies_in_install_includes = $(bin)dependencies_install_includes.in
#cmt_final_setup_install_includes = $(bin)WorkArea_install_includessetup.make
cmt_local_install_includes_makefile = $(bin)install_includes.make

else

cmt_final_setup_install_includes = $(bin)setup.make
cmt_dependencies_in_install_includes = $(bin)dependencies.in
#cmt_final_setup_install_includes = $(bin)WorkAreasetup.make
cmt_local_install_includes_makefile = $(bin)install_includes.make

endif

#cmt_final_setup = $(bin)setup.make
#cmt_final_setup = $(bin)WorkAreasetup.make

#install_includes :: ;

dirs ::
	@if test ! -r requirements ; then echo "No requirements file" ; fi; \
	  if test ! -d $(bin) ; then $(mkdir) -p $(bin) ; fi

javadirs ::
	@if test ! -d $(javabin) ; then $(mkdir) -p $(javabin) ; fi

srcdirs ::
	@if test ! -d $(src) ; then $(mkdir) -p $(src) ; fi

help ::
	$(echo) 'install_includes'

binobj = 
ifdef STRUCTURED_OUTPUT
binobj = install_includes/
#install_includes::
#	@if test ! -d $(bin)$(binobj) ; then $(mkdir) -p $(bin)$(binobj) ; fi
#	$(echo) "STRUCTURED_OUTPUT="$(bin)$(binobj)
endif

${CMTROOT}/src/Makefile.core : ;
ifdef use_requirements
$(use_requirements) : ;
endif

#-- end of make_header ------------------

#
#  We want to install all header files that follow the standard convention
#
#    ../<package>
#
#  into
#
#    ${CMTINSTALLAREA}/include/<package>/<package>
#
#  (with two levels of <package> directory)
#

ifeq ($(INSTALLAREA),)
installarea = $(CMTINSTALLAREA)
else
ifeq ($(findstring `,$(INSTALLAREA)),`)
installarea = $(shell $(subst `,, $(INSTALLAREA)))
else
installarea = $(INSTALLAREA)
endif
endif

install_include_dir = $(installarea)/include/$(package)

install_includes :: install_includesinstall

install :: install_includesinstall

install_includesinstall :: $(install_include_dir)

$(install_include_dir) ::
	@if test "$(install_include_dir)" = ""; then \
	  echo "Cannot install header files, no installation directory specified"; \
	else \
	  if test -d ../${package}; then \
	    here=`(cd ../${package}; pwd)`; \
	    need_new=yes; \
	    if test -L $(install_include_dir) ; then rm -f $(install_include_dir); fi; \
	    if test ! -d $(install_include_dir) ; then mkdir -p $(install_include_dir); fi; \
	    if test -L $(install_include_dir)/$(package); then \
	      eval d=$(install_include_dir)/$(package); \
	      dd=`ls -l $${d} | sed -e 's#.*[-][>]##'`; \
	      if test ! $${dd} = $${here}; then \
	        eval rm -Rf $(install_include_dir)/$(package) $(install_include_dir)/$(package).cmtref ; \
	      else \
	        need_new=no ; \
	      fi; \
	    fi; \
	    if test "$${need_new}" = "yes"; then \
	      echo "Installing files from standard ../${package} to $(install_include_dir)"; \
              eval ln -s $${here} $(install_include_dir)/$(package); \
              echo $${here} >|$(install_include_dir)/$(package).cmtref; \
	    else \
	      echo "Files from standard ../${package} already installed"; \
	    fi; \
	  else \
	    echo "No standard include file area"; \
	  fi; \
	fi

##	    (cd ../${package}; eval ln -s $(install_include_filter) $(install_include_dir));


##install_includesclean :: install_includesuninstall

uninstall :: install_includesuninstall

install_includesuninstall ::
	@if test "$(install_include_dir)" = ""; then \
	  echo "Cannot uninstall header files, no installation directory specified"; \
	else \
	  if test -d $(install_include_dir) ; then \
	    echo "Uninstalling files from $(install_include_dir)"; \
	    eval rm -rf $(install_include_dir) ; \
	  fi \
	fi


#-- start of cleanup_header --------------

clean :: install_includesclean ;
#	@cd .

ifndef PEDANTIC
.DEFAULT::
	$(echo) "(install_includes.make) $@: No rule for such target" >&2
else
.DEFAULT::
	$(error PEDANTIC: $@: No rule for such target)
endif

install_includesclean ::
#-- end of cleanup_header ---------------
