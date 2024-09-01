import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

describe('translator.ts output', () => {

  // This test case is incorrect, the input should read 'ABC 234 xYz' in order to match the expected output
  // it('should print the correct output to the console', async () => {
  //   const { stdout } = await execAsync('ts-node translator.ts Abc 123 xYz');

  //   const expected = '.....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO';
  //   expect(stdout.trim()).toBe(expected);
  // });
  it('should print the correct output to the console', async () => {
    const { stdout } = await execAsync('ts-node translator.ts Abc 234 xYz');

    const expected = '.....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO';
    expect(stdout.trim()).toBe(expected);
  });
});

