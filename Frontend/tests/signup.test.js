import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import AuthPage from '../path/to/AuthPage'; // Update the import path to where your AuthPage component is located.
import axios from 'axios';

// Mock axios to prevent actual API calls during tests
jest.mock('axios');

describe('AuthPage Signup', () => {
  beforeEach(() => {
    // Clear all mocks before each test
    axios.post.mockClear();
  });

  it('successfully signs up a new user', async () => {
    // Mock the API response for successful signup
    axios.post.mockResolvedValue({
      data: { id: 1, username: 'newuser' },
      status: 201
    });

    render(<AuthPage />);

    // Simulate user input
    userEvent.type(screen.getByPlaceholderText('Username'), 'newuser');
    userEvent.type(screen.getByPlaceholderText('Email'), 'newuser@example.com');
    userEvent.type(screen.getByPlaceholderText('Password'), 'password123');
    
    // Simulate form submission
    fireEvent.click(screen.getByRole('button', { name: /sign up/i }));

    // Wait for the expected outcome, e.g., a success message or redirection
    await waitFor(() => {
      expect(axios.post).toHaveBeenCalledWith(
        'http://localhost:8000/api/signup/', 
        {
          username: 'newuser',
          email: 'newuser@example.com',
          password: 'password123'
        }
      );
    });
  });
});
