import React from "react";

interface MealPlanComponentProps {
  mealPlan: { recipeName: string; calories: number }[];
}

const MealPlanComponent: React.FC<MealPlanComponentProps> = ({ mealPlan }) => {
  return (
    <div>
      <h2>Today's Meal Plan</h2>
      <ul>
        {mealPlan.map((recipe, index) => (
          <li key={index}>
            {recipe.recipeName} - {recipe.calories} calories
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MealPlanComponent;
