# Makefile
#
# RLE utilities: https://paradroid.automac.se/rle/

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


all: $(ODIR) $(ODIR)/viper_core.rle $(ODIR)/open_screen.rle viper

$(ODIR)/viper_core.bin: $(ODIR)/viper_core.o
	$(LD) $(LDFLAGS) -o $@ $^

$(ODIR)/open_screen.bin: $(ODIR)/open_screen.o
	$(LD) $(LDFLAGS) -o $@ $^

$(ODIR)/viper_core.rle: $(ODIR)/viper_core.bin

$(ODIR)/open_screen.rle: $(ODIR)/open_screen.bin

viper: $(ODIR)/viper.o
	$(LD) $(LDFLAGS) -o $@#064000 $^

.PHONY: clean

clean:
	$(RM) $(ODIR)/* viper#064000

$(ODIR):
	$(MD) $(ODIR)

$(ODIR)/%.o: $(SDIR)/%.c
	$(CC) $(CFLAGS) -o $(ODIR)/$(*).a65 $<
	$(AS) $(AFLAGS) -o $@ $(ODIR)/$(*).a65

$(ODIR)/%.o: $(SDIR)/%.a65
	$(AS) $(AFLAGS) -o $@ $<

$(ODIR)/%.rle: $(ODIR)/%.bin
	$(RLE) $< $@

$(ODIR)/%.bin: $(ODIR)/%.o
	$(LD) $(LDFLAGS) -o $@ $^
