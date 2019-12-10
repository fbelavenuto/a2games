# Makefile
#
# Uses the dos33fsutils from:
#  https://github.com/deater/dos33fsprogs

SYS = apple2

CC = cc65
AS = ca65
LD = ld65
AR = ar65
CP = cp
RM = rm -f
MD = mkdir

SDIR = src
ODIR = obj
LDIR = ../../apple2lib
IDIR = $(LDIR)/inc

CFLAGS  = -t $(SYS) -O -I$(IDIR) -I.
AFLAGS  = -t $(SYS) -l $(ODIR)/$(*).lst -I$(IDIR) -I.
LDFLAGS = -C $(LDIR)/_config


all: $(ODIR) bb bbmaker dsk

BB: $(ODIR)/bb.o
	$(LD) $(LDFLAGS) -o $@#064000 $^

BBMAKER: $(ODIR)/bbmaker.o
	$(LD) $(LDFLAGS) -o $@#061000 $^

dsk: bb bbmaker
	mkdos33fs -d data/tkdos_boot.bin BeautifulBoot.dsk
	dos33 BeautifulBoot.dsk save data/HELLO#FC0801
	dos33 BeautifulBoot.dsk save BBMAKER#061000
	dos33 BeautifulBoot.dsk save BB#064000
	dos33 BeautifulBoot.dsk save data/CB2K#066000

$(ODIR):
	$(MD) $(ODIR)

clean:
	$(RM) $(ODIR)/* *#06*

$(ODIR)/%.o: $(SDIR)/%.c
	$(CC) $(CFLAGS) -o $(ODIR)/$(*).a65 $<
	$(AS) $(AFLAGS) -o $@ $(ODIR)/$(*).a65

$(ODIR)/%.o: $(SDIR)/%.a65
	$(AS) $(AFLAGS) -o $@ $<
