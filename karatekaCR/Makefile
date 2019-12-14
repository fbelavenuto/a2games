# Makefile
#

SYS=apple2

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
IDIR = ../../apple2lib/inc

CFLAGS  = -t $(SYS) -O -I$(IDIR) -I.
AFLAGS  = -t $(SYS) -l $(ODIR)/$(*).lst -I$(IDIR) -I.
LDFLAGS = -C $(LDIR)/_config

all: $(ODIR) loader start piece1 piece2

loader: $(ODIR)/loader.o
	$(LD) $(LDFLAGS) -o 13LOADER#06E000 $^

start: $(ODIR)/start.o
	$(LD) $(LDFLAGS) -o 14START#06FDB3 $^
	
piece1:
	tkbinplay -d -w sine -r 44100 -p 3 -o "Karateka1_44_S_3.wav" "Karateka1.ini"
	flac -f "Karateka1_44_S_3.wav"
	tkbinplay -d -w sine -r 44100 -p 4 -o "Karateka1_44_S_4.wav" "Karateka1.ini"
	flac -f "Karateka1_44_S_4.wav"
	tkbinplay -d -w sine -r 48000 -p 3 -o "Karateka1_48_S_3.wav" "Karateka1.ini"
	flac -f "Karateka1_48_S_3.wav"
	tkbinplay -d -w sine -r 48000 -p 4 -o "Karateka1_48_S_4.wav" "Karateka1.ini"
	flac -f "Karateka1_48_S_4.wav"

piece2: 
	tkbinplay -a -d -w sine -r 44100 -p 3 -o "Karateka2_44_S_3.wav" "Karateka2.ini"
	flac -f "Karateka2_44_S_3.wav"
	tkbinplay -a -d -w sine -r 44100 -p 4 -o "Karateka2_44_S_4.wav" "Karateka2.ini"
	flac -f "Karateka2_44_S_4.wav"
	tkbinplay -a -d -w sine -r 48000 -p 3 -o "Karateka2_48_S_3.wav" "Karateka2.ini"
	flac -f "Karateka2_48_S_3.wav"
	tkbinplay -a -d -w sine -r 48000 -p 4 -o "Karateka2_48_S_4.wav" "Karateka2.ini"
	flac -f "Karateka2_48_S_4.wav"

clean:
	$(RM) $(ODIR)/* 

$(ODIR):
	$(MD) $(ODIR)

$(ODIR)/%.o: $(SDIR)/%.c
	$(CC) $(CFLAGS) -o $(ODIR)/$(*).s $<
	$(AS) $(AFLAGS) -o $@ $(ODIR)/$(*).s

$(ODIR)/%.o: $(SDIR)/%.a65
	$(AS) $(AFLAGS) -o $@ $<
