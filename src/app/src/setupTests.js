// jest-dom adds custom jest matchers for asserting on DOM nodes
import '@testing-library/jest-dom';

// Set up fetch for Node.js environment
global.fetch = require('jest-fetch-mock');
require('jest-fetch-mock').enableMocks();
