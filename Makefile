SSHELL     := bash 
MAKEFLAGS += --warn-undefined-variables
.SILENT: 
Root=$(shell git rev-parse --show-toplevel)


help          :  ## show help
	awk 'BEGIN {FS = ":.*?## "; print "\nmake [WHAT]" } \
			/^[^[:space:]].*##/ {printf "   \033[36m%-10s\033[0m : %s\n", $$1, $$2} \
			' $(MAKEFILE_LIST)

saved         : ## save and push to main branch 
	read -p "commit msg> " x; y=$${x:-saved}; git commit -am "$$y}"; git push;  git status; echo "$$y, saved!"
 

FILES=$(wildcard *.py)
docs: 
	echo "docs..."
	$(MAKE) -B $(addprefix ~/tmp/, $(FILES:.py=.pdf))  $(addprefix ../docs/, $(FILES:.py=.html))
 
~/tmp/%.pdf   : %.py  ## py ==> pdf
	mkdir -p ~/tmp
	echo "$@" 
	a2ps                           \
		-qBr                         \
		--chars-per-line 100           \
		--file-align=fill               \
		--line-numbers=1                 \
		--borders=no                      \
		--pro=color                        \
		--columns  3                        \
		-M letter                            \
		-o ~/tmp/$^.ps $^ ;                   \
	ps2pdf ~/tmp/$^.ps $@ ;  rm ~/tmp/$^.ps; \

name:
	read -p "word> " w; figlet -f mini -W $$w  | gawk '$$0 {print "#        "$$0}' |pbcopy

install:
	pip install -e .

R=20


bores=~/gits/txt/aa24/data/Process/small

X=-p10000-d27-o4-dataset1

bore:
	$(MAKE) -j 8 -B  \
	  ../out/xomo_flight.out ../out/xomo_ground.out ../out/xomo_osp.out ../out/xomo_osp2.out \
		../out/pom3a.out ../out/pom3b.out ../out/pom3c.out ../out/pom3d.out  

flashes=~/gits/txt/aa24/data/flash

flash:
	$(MAKE) -j 8 -B ../out/SS-A.out ../out/SS-B.out ../out/SS-C.out ../out/SS-D.out ../out/SS-E.out  \
					../out/SS-F.out ../out/SS-G.out ../out/SS-H.out ../out/SS-I.out ../out/SS-J.out  \
					../out/SS-K.out ../out/SS-L.out ../out/SS-M.out ../out/SS-N.out ../out/SS-O.out 

usuals=../data
usual:
	$(MAKE) -j 8 -B ../out/auto93.out   ../out/healthCloseIsses12mths0001-hard.out     \
					../out/china.out   ../out/healthCloseIsses12mths0011-easy.out \
				../out/coc1000.out ../out/nasa93dem.out  ../out/pom.out

$(Root)/out/%.out : $(usuals)/%.csv
	echo "-- $@"; python3 eg.py -R $R -f $^ -t smoy | tee $@

$(Root)/out/%.out : $(bores)/%.csv
	echo $^
	echo "-- $@"; python3 eg.py -R $R -f $^ -t smoy | tee $@

$(Root)/out/%.out : $(flashes)/%.csv
	echo "-- $@"; python3 eg.py -R $R -f $^ -t smoy | tee $@
