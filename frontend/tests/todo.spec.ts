import { test, expect } from '@playwright/test';

test.describe('Todo App', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000');
  });

  test('should allow me to add a new todo item', async ({ page }) => {
    // Create a new todo item
    await page.locator('input[placeholder="Add a new task..."]').fill('Buy milk');
    await page.locator('button[type="submit"]').click();

    // Make sure the new item is in the list
    await expect(page.locator('text=Buy milk')).toBeVisible();
  });

  test('should allow me to mark an item as completed', async ({ page }) => {
    // Add a new item first
    await page.locator('input[placeholder="Add a new task..."]').fill('Walk the dog');
    await page.locator('button[type="submit"]').click();

    // Mark the item as completed
    await page.locator('text=Walk the dog').click();

    // Verify the item is marked as completed
    await expect(page.locator('text=Walk the dog')).toHaveClass(/line-through/);
  });

  test('should allow me to delete a todo item', async ({ page }) => {
    // Add a new item first
    await page.locator('input[placeholder="Add a new task..."]').fill('Clean the house');
    await page.locator('button[type="submit"]').click();

    // Delete the item
    await page.locator('li:has-text("Clean the house") >> button').click();

    // Verify the item is no longer in the list
    await expect(page.locator('text=Clean the house')).not.toBeVisible();
  });
});
