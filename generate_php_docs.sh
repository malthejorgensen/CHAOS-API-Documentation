for f in $(find ../../CHAOS.Portal.Client-PHP/src/ -iname '*.php' -print0)
do
  echo "$f"; bf="$(basename $f)"
  doxphp < $f | doxphp2sphinx > docs/$bf.rst
done
