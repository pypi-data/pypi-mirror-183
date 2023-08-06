
      program moogsynth
c******************************************************************************
c     This is the main driver for the non-interactive version of MOOG.  
c     It reads the parameter file and sends MOOG to various controlling 
c     subroutines.  In this version of MOOG the parameter file must
c     be named "batch.par" (because the code cannot stop to ask the
c     user to name the parameter file)
c******************************************************************************

      include 'Atmos.com'
      include 'Pstuff.com'
      character temp*100

c$$$$$$$$$$$$$$$$$$$$$$$$ USER SETUP AREA $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
c     in compiling MOOG, here the various machine-specific things are
c     declared.  First, define the directory where MOOG lives, in order to
c     be able to pull in auxiliary data files; executing 'make' will
c     generate a reminder of this
      write (moogpath,1001)
      moogpath = 
     .  '$SRCDIR'

c*****What kind of machine are you using?  Possible ones are:
c     "mac" = Intel-based Apple Mac
c     "pcl" = a PC or desktop running some standard linux like Redhat
c     "uni" = a machine running Unix, specifically Sun Solaris
      machine = "$MACHINE"


c*****for x11 terminal types, define the parameters of plotting windows;
c     set up an x11 screen geometry and placement that is good for spectrum
c     syntheses (long, but not tall); the user should play with the format
c     statements for particular machines.
      write (smt1,1018)
c     now do the same for line abundance trend plots (short but tall).
      write (smt2,1017)
c$$$$$$$$$$$$$$$$$$$$$$$ END OF USER SETUP $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


c*****declare this to be the non-interactive version; variable "silent"
c     will be queried on all occasions that might call for user input;
c     DON'T CHANGE THIS VARIABLE; 
c     if silent = 'n', the normal interactive MOOG is run;
c     if silent = 'y', the non-interactive MOOG is run
      silent = 'y'


c*****invoke the overall starting routine
      control = '       '
      call begin

      If (fparam .eq. 'error') then
        temp = 'Please specify the input parameter file at the command'
        write (*,444) temp
444     format (A100)
        return
      endif

c*****use one of the standard driver routines ("isotop" is obsolete): 
c      if     (control .eq. 'synplot') then
c         call plotit
c      elseif (control .eq. 'isoplot') then
c         call plotit
c      elseif (control .eq. 'synth  ') then
c  ##### SYNTH ONLY #####
         call synth
c      elseif (control .eq. 'cogsyn ') then
c         call cogsyn  
c      elseif (control .eq. 'blends ') then
c         call blends  
c      elseif (control .eq. 'abfind ') then
c         call abfind
c      elseif (control .eq. 'ewfind ') then
c         call ewfind
c      elseif (control .eq. 'cog    ') then
c         call cog
c      elseif (control .eq. 'calmod ') then
c         call calmod
c      elseif (control .eq. 'isotop ') then
c         control = 'synth  '
c         call synth
c      elseif (control .eq. 'doflux ') then
c         call doflux   
c      elseif (control .eq. 'weedout') then
c         call weedout  
c      elseif (control .eq. 'gridsyn') then
c         call gridsyn  
c      elseif (control .eq. 'gridplo') then
c         call gridplo  
c      elseif (control .eq. 'binary ') then
c         call binary
c      elseif (control .eq. 'abpop  ') then
c         call abpop
c      elseif (control .eq. 'synpop ') then
c         call synpop


c*****or, put in your own drivers in the form below....
c      elseif (control .eq. 'mine  ') then
c         call  mydriver 


c*****or else you are out of luck!
c      else
c         array = 'THIS IS NOT ONE OF THE DRIVERS. I QUIT!'
c         istat = ivwrite (4,3,array,49)
c         stop
c      endif


c*****format statements
1001  format (60(' '))
1017  format ('x11 -bg black -title MOOGplot -geom 700x800+650+000')
1018  format ('x11 -bg black -title MOOGplot -geom 1200x400+20+450')


      end
      
