/**
 * Array utility functions for common operations.
 */

/**
 * Remove duplicate values from an array.
 * 
 * @param {Array} arr - Array with possible duplicates
 * @returns {Array} Array with unique values
 * 
 * @example
 * const numbers = [1, 2, 2, 3, 4, 4, 5];
 * const unique = removeDuplicates(numbers);
 * console.log(unique); // [1, 2, 3, 4, 5]
 */
function removeDuplicates(arr) {
  return [...new Set(arr)];
}

/**
 * Chunk an array into smaller arrays of specified size.
 * 
 * @param {Array} arr - Array to chunk
 * @param {number} size - Size of each chunk
 * @returns {Array} Array of chunks
 * 
 * @example
 * const numbers = [1, 2, 3, 4, 5, 6, 7];
 * const chunks = chunkArray(numbers, 3);
 * console.log(chunks); // [[1, 2, 3], [4, 5, 6], [7]]
 */
function chunkArray(arr, size) {
  const chunks = [];
  for (let i = 0; i < arr.length; i += size) {
    chunks.push(arr.slice(i, i + size));
  }
  return chunks;
}

/**
 * Flatten a nested array by one level.
 * 
 * @param {Array} arr - Nested array
 * @returns {Array} Flattened array
 * 
 * @example
 * const nested = [[1, 2], [3, 4], [5]];
 * const flat = flattenArray(nested);
 * console.log(flat); // [1, 2, 3, 4, 5]
 */
function flattenArray(arr) {
  return arr.flat();
}

module.exports = {
  removeDuplicates,
  chunkArray,
  flattenArray
};
