/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let res=0;
    for(let i = 0; i < args.length; i++){
        res += 1
    }
    return res;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */