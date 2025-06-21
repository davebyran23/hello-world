// Dynamic Greeter JavaScript Implementation
// Replicates the Python logic for web interface

function getCurrentTimeInfo() {
    const now = new Date();
    const hour = now.getHours();
    const dayName = now.toLocaleDateString('en-US', { weekday: 'long' });
    const monthName = now.toLocaleDateString('en-US', { month: 'long' });
    const dayNumber = now.getDate();
    
    return { hour, dayName, monthName, dayNumber };
}

function getTimeGreeting(hour) {
    if (hour >= 5 && hour < 12) {
        return "Good morning";
    } else if (hour >= 12 && hour < 17) {
        return "Good afternoon";
    } else if (hour >= 17 && hour < 21) {
        return "Good evening";
    } else {
        return "Good night";
    }
}

function getSpecialGreeting(name) {
    const nameLower = name.toLowerCase();
    
    const specialGreetings = {
        "david": "Hey there, AI Director! 🎉",
        "admin": "Welcome back, Administrator! 🔐",
        "guest": "Hello, welcome to our system! 👋",
        "alice": "Wonderful to see you, Alice! ✨",
        "bob": "Hey Bob, great to have you here! 🚀"
    };
    
    return specialGreetings[nameLower] || null;
}

function getDayEnthusiasm(dayName) {
    const dayEnthusiasm = {
        "Monday": "Let's start the week strong! 💪",
        "Tuesday": "Tuesday energy is flowing! ⚡",
        "Wednesday": "Hump day - we're halfway there! 🐪",
        "Thursday": "Almost Friday - keep going! 🎯",
        "Friday": "TGIF! Weekend is almost here! 🎉",
        "Saturday": "Perfect day for relaxation! 😌",
        "Sunday": "Sunday vibes - recharge time! 🌅"
    };
    
    return dayEnthusiasm[dayName] || "Have a wonderful day! 🌟";
}

function createDynamicGreeting(name, timeInfo) {
    const { hour, dayName, monthName, dayNumber } = timeInfo;
    
    // Get base time greeting
    const timeGreeting = getTimeGreeting(hour);
    
    // Check for special name greeting
    const specialGreeting = getSpecialGreeting(name);
    
    let greeting;
    if (specialGreeting) {
        greeting = specialGreeting;
    } else {
        greeting = `${timeGreeting}, ${name}!`;
    }
    
    // Add day-specific enthusiasm
    const dayMessage = getDayEnthusiasm(dayName);
    
    // Add date information
    const dateInfo = `Today is ${dayName}, ${monthName} ${dayNumber}`;
    
    return { greeting, dayMessage, dateInfo };
}

function generateGreeting() {
    const userNameInput = document.getElementById('userName');
    const userName = userNameInput.value.trim();
    
    if (!userName) {
        alert('Please enter your name!');
        return;
    }
    
    // Get current time information
    const timeInfo = getCurrentTimeInfo();
    
    // Create dynamic greeting
    const { greeting, dayMessage, dateInfo } = createDynamicGreeting(userName, timeInfo);
    
    // Display the greeting
    document.getElementById('greetingText').textContent = greeting;
    document.getElementById('dayMessage').textContent = dayMessage;
    document.getElementById('dateInfo').textContent = dateInfo;
    
    // Generate and display stats
    const statsContent = document.getElementById('statsContent');
    const currentTime = new Date().toLocaleTimeString('en-US', { 
        hour: 'numeric', 
        minute: '2-digit',
        hour12: true 
    });
    
    statsContent.innerHTML = `
        <div class="stat-item">
            <div class="stat-label">Name Length</div>
            <div class="stat-value">${userName.length} characters</div>
        </div>
        <div class="stat-item">
            <div class="stat-label">Current Time</div>
            <div class="stat-value">${currentTime}</div>
        </div>
        <div class="stat-item">
            <div class="stat-label">Time of Day</div>
            <div class="stat-value">${getTimeGreeting(timeInfo.hour).toLowerCase()}</div>
        </div>
        <div class="stat-item">
            <div class="stat-label">Day of Week</div>
            <div class="stat-value">${timeInfo.dayName}</div>
        </div>
    `;
    
    // Show the output section with animation
    const outputSection = document.getElementById('outputSection');
    outputSection.style.display = 'block';
    outputSection.scrollIntoView({ behavior: 'smooth', block: 'center' });
    
    // Add some visual feedback
    const greetBtn = document.getElementById('greetBtn');
    greetBtn.textContent = 'Greeting Generated! ✨';
    setTimeout(() => {
        greetBtn.textContent = 'Get Greeting';
    }, 2000);
}

// Add keyboard support for Enter key
document.getElementById('userName').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        generateGreeting();
    }
});

// Add some interactive effects
document.addEventListener('DOMContentLoaded', function() {
    // Add loading animation to the page
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
    
    // Add hover effects to the input
    const userNameInput = document.getElementById('userName');
    userNameInput.addEventListener('focus', function() {
        this.parentElement.style.transform = 'scale(1.02)';
    });
    
    userNameInput.addEventListener('blur', function() {
        this.parentElement.style.transform = 'scale(1)';
    });
}); 