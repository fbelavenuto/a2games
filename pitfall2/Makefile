# Makefile
#

SYS = apple2

CC = cc65
AS = ca65
LD = ld65
AR = ar65
CP = cp
RM = rm -f
MD = mkdir
RLE = rlepack

SDIR = src
ODIR = obj
LDIR = ../../apple2lib
IDIR = $(LDIR)/inc

CFLAGS  = -t $(SYS) -O -I$(IDIR) -I.
AFLAGS  = -t $(SYS) -l $(ODIR)/$(*).lst -I$(IDIR) -I.
LDFLAGS = -C $(LDIR)/_config


all: $(ODIR) pitfall2

OBJS = $(ODIR)/pitfall2.o

pitfall2: $(OBJS)
	$(LD) $(LDFLAGS) -o $@#0608F0 $^


clean:
	$(RM) ODIR/* pitfall2#0608F0

$(ODIR)/%.o: $(SDIR)/%.c
	$(CC) $(CFLAGS) -o $(ODIR)/$(*).a65 $<
	$(AS) $(AFLAGS) -o $@ $(ODIR)/$(*).a65

$(ODIR)/%.o: $(SDIR)/%.a65
	$(AS) $(AFLAGS) -o $@ $<
