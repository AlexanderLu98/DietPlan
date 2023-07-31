import React, { useState } from "react";
import "./App.css";
import SearchComponent from "./components/SearchComponent";
import MealPlanComponent from "./components/MealPlanComponent";
import generateMealPlan from "./components/MealPlanGenerator";

const App: React.FC = () => {
  const [mealPlan, setMealPlan] = useState<any[]>([]);

  const handleSearch = (searchQuery: string) => {
    // Parse the search query into a number (assuming it's a daily calorie goal).
    const calorieGoal = parseInt(searchQuery, 10);

    // Check if the calorieGoal is a valid number.
    if (!isNaN(calorieGoal)) {
      // Generate the meal plan based on the calorie goal using the mealPlanGenerator function.
      const generatedMealPlan = generateMealPlan(calorieGoal);
      setMealPlan(generatedMealPlan);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Diet Plan Website</h1>
        <SearchComponent onSearch={handleSearch} />
        {mealPlan.length > 0 && <MealPlanComponent mealPlan={mealPlan} />}
      </header>
    </div>
  );
};

export default App;
