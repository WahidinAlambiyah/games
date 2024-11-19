const defaultValues = ['$100', '$200', '$300', '$400', '$500', '$600'];
let wheelValues = loadWheelValues();
let prizeHistory = loadPrizeHistory();

const randomPrizes = [
  '10 min back massage',
  'Dinner date at favorite place',
  'Movie night of choice',
  'No chores for a day',
  'Breakfast in bed',
  'One free wish',
  'Day off from cooking',
  'Coffee date on me',
  'Surprise gift',
  'Outdoor picnic'
];

function ensureMinSegments(items, minSegments = 6) {
    const itemCount = items.length;
    if (itemCount < minSegments) {
      const repeats = Math.ceil(minSegments / itemCount);
      return Array.from({ length: minSegments }, (_, i) => items[i % itemCount]);
    }
    return items;
  }

function loadWheelValues() {
  const savedValues = localStorage.getItem('wheelValues');
  return savedValues ? JSON.parse(savedValues) : [...defaultValues];
}

function saveWheelValues() {
  localStorage.setItem('wheelValues', JSON.stringify(wheelValues));
}

function loadPrizeHistory() {
  const savedHistory = localStorage.getItem('prizeHistory');
  return savedHistory ? JSON.parse(savedHistory) : [];
}

function savePrizeHistory() {
  localStorage.setItem('prizeHistory', JSON.stringify(prizeHistory));
}

function addItem() {
  const input = document.getElementById('wheel-input');
  const value = input.value.trim();
  if (value && !wheelValues.includes(value)) { 
    wheelValues.push(value);
    saveWheelValues();
    input.value = '';
    updateWheelList();
    updateItemList();
  } else {
    alert("This value is already in the wheel or empty. Please add a unique value.");
  }
}

function addList() {
  const input = document.getElementById('wheel-list-input');
  const values = input.value.split(',').map(item => item.trim()).filter(item => item);
  const uniqueValues = values.filter(value => !wheelValues.includes(value));
  if (uniqueValues.length > 0) {
    wheelValues.push(...uniqueValues);
    saveWheelValues();
    input.value = '';
    updateWheelList();
    updateItemList();
  } else {
    alert("All values are duplicates or empty. Please add unique values.");
  }
}

function deleteItem(index) {
  wheelValues.splice(index, 1);
  saveWheelValues();
  updateWheelList();
  updateItemList();
}

function editItem(index) {
  const newValue = prompt("Edit item:", wheelValues[index]);
  if (newValue && !wheelValues.includes(newValue)) {
    wheelValues[index] = newValue;
    saveWheelValues();
    updateWheelList();
    updateItemList();
  } else {
    alert("This value is already in the wheel or empty. Please enter a unique value.");
  }
}

const MIN_SEGMENTS = 6;  // Minimum number of segments for a full wheel

function updateWheelList() {
    const wheelList = document.getElementById('wheel-list');
    if (!wheelList) {
      console.warn("Element with id 'wheel-list' not found.");
      return;
    }
    wheelList.innerHTML = '';
  
    const items = ensureMinSegments(wheelValues);
    const angle = 360 / items.length;
  
    items.forEach((value, index) => {
      const li = document.createElement('li');
      li.textContent = value;
      li.style.transform = `rotate(${index * angle}deg) skewY(-${90 - angle / 2}deg)`; // Dynamic skew for pie effect
      wheelList.appendChild(li);
    });
  }

  function updateItemList() {
    const itemList = document.getElementById('item-list');
    if (!itemList) {
      console.warn("Element with id 'item-list' not found.");
      return;
    }
  
    itemList.innerHTML = '';
  
    wheelValues.forEach((value, index) => {
      const item = document.createElement('li');
      item.textContent = value;
  
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Delete';
      deleteButton.onclick = () => deleteItem(index);
  
      const editButton = document.createElement('button');
      editButton.textContent = 'Edit';
      editButton.onclick = () => editItem(index);
  
      item.appendChild(editButton);
      item.appendChild(deleteButton);
      itemList.appendChild(item);
    });
  }
  

function updatePrizeHistory() {
  const prizeHistoryList = document.getElementById('prize-history');
  prizeHistoryList.innerHTML = '';

  prizeHistory.forEach((prize, index) => {
    const item = document.createElement('li');
    item.textContent = prize;

    const addButton = document.createElement('button');
    addButton.textContent = 'Add to Wheel';
    addButton.onclick = () => addPrizeBackToWheel(prize, index);
    addButton.disabled = wheelValues.includes(prize); 

    item.appendChild(addButton);
    prizeHistoryList.appendChild(item);
  });
}

function addPrizeBackToWheel(prize, index) {
  if (!wheelValues.includes(prize)) { 
    wheelValues.push(prize);
    saveWheelValues();
    updateWheelList();
    updateItemList();
  }
}

function wheelOfFortune(selector) {
  const node = document.querySelector(selector);
  if (!node) return;

  const spin = node.querySelector('button');
  const wheel = node.querySelector('ul');
  let animation;
  let previousEndDegree = 0;

  spin.addEventListener('click', () => {
    if (animation) {
      animation.cancel();
    }

    const randomAdditionalDegrees = Math.random() * 360 + 1800;
    const newEndDegree = previousEndDegree + randomAdditionalDegrees;

    animation = wheel.animate([
      { transform: `rotate(${previousEndDegree}deg)` },
      { transform: `rotate(${newEndDegree}deg)` }
    ], {
      duration: 4000,
      direction: 'normal',
      easing: 'cubic-bezier(0.440, -0.205, 0.000, 1.130)',
      fill: 'forwards',
      iterations: 1
    });

    animation.onfinish = () => {
      const degrees = newEndDegree % 360;
      const sliceAngle = 360 / wheelValues.length;
      const winningIndex = Math.floor((360 - degrees) / sliceAngle) % wheelValues.length;
      
      const prize = wheelValues[winningIndex];
      showModal(`You won: ${prize}!`);
      
      prizeHistory.push(prize);
      savePrizeHistory();
      
      wheelValues.splice(winningIndex, 1);
      saveWheelValues();
      
      updateWheelList();
      updateItemList();
      updatePrizeHistory();
    };

    previousEndDegree = newEndDegree;
  });
}

function showModal(message) {
  document.getElementById('result-text').textContent = message;
  document.getElementById('result-modal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('result-modal').style.display = 'none';
}

function toggleVisibility(elementId) {
  const element = document.getElementById(elementId);
  element.classList.toggle("hidden");
}

function clearPrizeHistory() {
  prizeHistory = [];
  savePrizeHistory();
  updatePrizeHistory();
}

function generatePrizes() {
  wheelValues = [...randomPrizes];
  saveWheelValues();
  updateWheelList();
  updateItemList();
}

document.addEventListener('DOMContentLoaded', () => {
  updateWheelList();
  updateItemList();
  updatePrizeHistory();
  wheelOfFortune('.ui-wheel-of-fortune');
});
