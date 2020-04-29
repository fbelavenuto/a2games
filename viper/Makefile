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

SDIR = src
ODIR = obj
LDIR = ../../apple2lib
IDIR = $(LDIR)/inc

CFLAGS  = -t $(SYS) -O -I$(IDIR) -I.
AFLAGS  = -t $(SYS) -l $(ODIR)/$(*).lst -I$(IDIR) -I.
LDFLAGS = -C $(LDIR)/_config


all: $(ODIR) dsk

VIPER: $(ODIR)/viper.o
	$(LD) $(LDFLAGS) -o $@#062000 $^

dsk: VIPER
	dos33util "Viper.dsk" init data\TKDOS33.bin
	dos33util "Viper.dsk" save data\HELLO#FC0801
	dos33util "Viper.dsk" save VIPER#062000

.PHONY: clean

clean:
	$(RM) $(ODIR)/* VIPER#062000

$(ODIR):
	$(MD) $(ODIR)

$(ODIR)/%.o: $(SDIR)/%.c
	$(CC) $(CFLAGS) -o $(ODIR)/$(*).a65 $<
	$(AS) $(AFLAGS) -o $@ $(ODIR)/$(*).a65

$(ODIR)/%.o: $(SDIR)/%.a65
	$(AS) $(AFLAGS) -o $@ $<

$(ODIR)/%.bin: $(ODIR)/%.o
	$(LD) $(LDFLAGS) -o $@ $^
