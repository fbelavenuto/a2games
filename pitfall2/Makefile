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
CT2UTL = ct2utils

SDIR = src
ODIR = obj
LDIR = ../../apple2lib
IDIR = $(LDIR)/inc

CFLAGS  = -t $(SYS) -O -I$(IDIR) -I.
AFLAGS  = -t $(SYS) -l $(ODIR)/$(*).lst -I$(IDIR) -I.
LDFLAGS = -C $(LDIR)/_config


all: $(ODIR) ct2

OBJS1 = $(ODIR)/tk2k_ar.o
OBJS2 = $(ODIR)/pitfall2.o

tk2k_ar: $(OBJS1)
	$(LD) $(LDFLAGS) -o $@#060036 $^

PITFALL2: $(OBJS2)
	$(LD) $(LDFLAGS) -o $@#0608FD $^

ct2: tk2k_ar PITFALL2
	$(CT2UTL) "Pit Fall II - Lost Caverns(C).ct2" -c
	$(CT2UTL) "Pit Fall II - Lost Caverns(C).ct2" -i -f tk2k_ar#060036 -t PITFII
	$(CT2UTL) "Pit Fall II - Lost Caverns(C).ct2" -i -f PITFALL2#0608FD -t PITFII
#	dos33util "Pit Fall II - Lost Caverns(C).dsk" init data\TKDOS2000.bin
#	dos33util "Pit Fall II - Lost Caverns(C).dsk" save data\HELLO#FC0801
#	dos33util "Pit Fall II - Lost Caverns(C).dsk" save PITFALL2#0608FD
#	ct2utils "Pit Fall II - Lost Caverns(C).ct2" -w -f "Pit Fall II - Lost Caverns(C).wav"
#	flac -f "Pit Fall II - Lost Caverns(C).wav"
#	tkbinplay -d -w sine -r 44100 -p 3 -o "Pit Fall II - Lost Caverns(C)_44_S_3.wav" "data\Pit Fall II - Lost Caverns(C).ini"
#	flac -f "Pit Fall II - Lost Caverns(C)_44_S_3.wav"
#	tkbinplay -d -w sine -r 44100 -p 4 -o "Pit Fall II - Lost Caverns(C)_44_S_4.wav" "data\Pit Fall II - Lost Caverns(C).ini"
#	flac -f "Pit Fall II - Lost Caverns(C)_44_S_4.wav"
#	tkbinplay -d -w sine -r 48000 -p 3 -o "Pit Fall II - Lost Caverns(C)_48_S_3.wav" "data\Pit Fall II - Lost Caverns(C).ini"
#	flac -f "Pit Fall II - Lost Caverns(C)_48_S_3.wav"
#	tkbinplay -d -w sine -r 48000 -p 4 -o "Pit Fall II - Lost Caverns(C)_48_S_4.wav" "data\Pit Fall II - Lost Caverns(C).ini"
#	flac -f "Pit Fall II - Lost Caverns(C)_48_S_4.wav"
#	$(RM) *.wav
	
$(ODIR):
	$(MD) $(ODIR)

clean:
	$(RM) $(ODIR)/* tk2k_ar#060036 PITFALL2#0608FD *.flac *.dsk *.ct2

$(ODIR)/%.o: $(SDIR)/%.c
	$(CC) $(CFLAGS) -o $(ODIR)/$(*).a65 $<
	$(AS) $(AFLAGS) -o $@ $(ODIR)/$(*).a65

$(ODIR)/%.o: $(SDIR)/%.a65
	$(AS) $(AFLAGS) -o $@ $<
