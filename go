#python -i lefdefsvg.py -slef component.slef -sdef circuit.sdef -o tmp4.svg
python lefdefsvg.py -slef component.slef -sdef circuit.sdef -o tmp4.svg
cat svg_header > output.svg
cat tmp4.svg >> output.svg
cat svg_footer >> output.svg
open -a Safari output.svg

