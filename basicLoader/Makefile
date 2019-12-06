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

all: $(ODIR) BasicLoaderPag1 BasicLoaderPag2

BasicLoaderPag1:
	$(AS) $(AFLAGS) -D PAG1 -o $(ODIR)/basicLoader.o $(SDIR)/basicLoader.a65
	$(LD) $(LDFLAGS) -o $@.bin $(ODIR)/basicLoader.o

BasicLoaderPag2:
	$(AS) $(AFLAGS) -D PAG2 -o $(ODIR)/basicLoader.o $(SDIR)/basicLoader.a65
	$(LD) $(LDFLAGS) -o $@.bin $(ODIR)/basicLoader.o

clean:
	$(RM) $(ODIR)/* *.bin

$(ODIR)/%.o: $(SDIR)/%.c
	$(CC) $(CFLAGS) -o $(ODIR)/$(*).a65 $<
	$(AS) $(AFLAGS) -o $@ $(ODIR)/$(*).a65

$(ODIR)/%.o: $(SDIR)/%.a65
	$(AS) $(AFLAGS) -o $@ $<
