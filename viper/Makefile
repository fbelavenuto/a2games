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
CT2UTL = ct2utils
DOSUTL = dos33util

SDIR = src
ODIR = obj
LDIR = ../../apple2lib
IDIR = $(LDIR)/inc

CFLAGS  = -t $(SYS) -O -I$(IDIR) -I.
AFLAGS  = -t $(SYS) -I$(IDIR) -I.
LDFLAGS = -C $(LDIR)/_config


all: $(ODIR) viper_a2 tk2k_ar viper_tk2k

viper_a2: $(ODIR)/viper_a2.o
	$(LD) $(LDFLAGS) -o VIPER#062000 $^
	$(DOSUTL) "Viper_A2.dsk" init data\TKDOS33.bin
	$(DOSUTL) "Viper_A2.dsk" save data\HELLO#FC0801
	$(DOSUTL) "Viper_A2.dsk" save VIPER#062000

tk2k_ar: $(ODIR)/tk2k_ar.o
	$(LD) $(LDFLAGS) -o $@#060036 $^

viper_tk2k: $(ODIR)/viper_tk2k.o
	$(LD) $(LDFLAGS) -o VIPER#062000 $^
	$(DOSUTL) "Viper_TK2K.dsk" init data\TKDOS2000.bin
	$(DOSUTL) "Viper_TK2K.dsk" save data\HELLO#FC0801
	$(DOSUTL) "Viper_TK2K.dsk" save VIPER#062000
	$(CT2UTL) "Viper.ct2" -c
	$(CT2UTL) "Viper.ct2" -i -f tk2k_ar#060036 -t VIPER
	$(CT2UTL) "Viper.ct2" -i -f VIPER#062000 -t VIPER


.PHONY: clean

clean:
	$(RM) $(ODIR)/* tk2k_ar#060036 VIPER#062000 *.ct2 *.dsk

$(ODIR):
	$(MD) $(ODIR)

$(ODIR)/viper_a2.o: $(SDIR)/viper.a65
	$(AS) $(AFLAGS) -l $(ODIR)/viper_a2.lst -DMACHINE=0 -o $@ $<

$(ODIR)/viper_tk2k.o: $(SDIR)/viper.a65
	$(AS) $(AFLAGS) -l $(ODIR)/viper_tk2k.lst -DMACHINE=1 -o $@ $<

$(ODIR)/tk2k_ar.o: $(SDIR)/tk2k_ar.a65
	$(AS) $(AFLAGS) -l $(ODIR)/tk2k_ar.lst -o $@ $<

