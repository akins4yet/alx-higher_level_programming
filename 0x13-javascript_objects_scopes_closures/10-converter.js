#!/us/rbin/node

rts.converter = function (base) {
  function convert (n) {
    return n.toString(base);
  }
  return convert;
};
