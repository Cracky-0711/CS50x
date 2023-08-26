document.addEventListener('DOMContentLoaded', function() {
    const menuButtons = document.querySelectorAll('.menu-btn');
    
    menuButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.stopPropagation();
            const menuContent = this.nextElementSibling;
            menuContent.style.display = (menuContent.style.display === 'block') ? 'none' : 'block';
        });
    });

    document.addEventListener('click', function() {
        const openMenus = document.querySelectorAll('.menu-content[style="display: block;"]');
        openMenus.forEach(menu => {
            menu.style.display = 'none';
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const showUncompletedCheckbox = document.getElementById('showUncompleted');
    const showInProgressCheckbox = document.getElementById('showInProgress');
    const showCompletedCheckbox = document.getElementById('showCompleted');
    const tasks = document.querySelectorAll('.task');

    function updateTaskVisibility() {
        const uncompletedChecked = showUncompletedCheckbox.checked;
        const inProgressChecked = showInProgressCheckbox.checked;
        const completedChecked = showCompletedCheckbox.checked;

        tasks.forEach(task => {
            const status = task.querySelector('.task-status').textContent.trim().toLowerCase();
            task.style.display =
                (uncompletedChecked && status === 'incomplete') ||
                (inProgressChecked && status === 'inprogress') ||
                (completedChecked && status === 'completed')
                    ? 'flex'
                    : 'none';
        });
    }

    showUncompletedCheckbox.addEventListener('change', updateTaskVisibility);
    showInProgressCheckbox.addEventListener('change', updateTaskVisibility);
    showCompletedCheckbox.addEventListener('change', updateTaskVisibility);

    // 初期表示時に実行
    updateTaskVisibility();
});
