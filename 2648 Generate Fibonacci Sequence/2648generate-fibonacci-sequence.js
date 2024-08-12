/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {

   let n1 = 0
   let n2 = 1

    // n1 = 0, n2 = 1
    // n1 = 1, n2 = 1
    // n1 = 1, n2 = 2
    // n1 = 2, n2 = 3
   while(true) {
    yield n1
    const next = n1 + n2;
    n1 = n2
    n2 = next
   }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */