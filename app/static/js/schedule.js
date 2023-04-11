  // document.addEventListener('DOMContentLoaded', function() {
  //   var calendarEl = document.getElementById('calendar');
  //   var filterStatusBtn = document.querySelector('#filter-status');
  //   var filterEmployeeBtn = document.querySelector('#filter-employee');
  //   var filterDateBtn = document.querySelector('#filter-date');



  //   var calendar = new FullCalendar.Calendar(calendarEl, {
  //     initialView: 'dayGridMonth',
  //     editable: true,
  //     selectable: true,
  //     height: 550,
  //     select: function(selectionInfo){
  //       console.log(selectionInfo);
  //     },
  //     events : [
  //       {title: 'Meeting', start: new Date(), status: "in progress", employee: "Associated Employee 1", customer: "Associated Customer 1"},
  //       {title: 'Meeting2', start: new Date(2023,4,5), status: "in progress", employee: "Associated Employee 2", customer: "Associated Customer 2"}
  //     ],
  //     eventDrop: function(event,dayDelta,minuteDelta,allDay,revertFunc) {
  //       alert(
  //         event.event.title + " was moved "
  //       );

  //       if (!confirm("Are you sure about this change?")) {
  //           revertFunc();
  //       }
  //   },
  //   eventClick: function(event, revertFunc){
  //     event_title = event.event.title
  //     new_title = prompt("Enter new title")
  //     if(new_title){
  //       event.event.setProp('title', new_title)     
  //     }
  //     if (!confirm("Are you sure you want to change the title?")) {
  //       revertFunc();
  //   }
  //   }
  //   });
  //   calendar.render();

  //   filterStatusBtn.addEventListener('click', () => {
  //     status_filter = prompt("Which status do you want to filter by?")
  //     all_events = calendar.getEvents()
  //     events_lst = []   

  //     for(ev of all_events){
  //       if(ev.extendedProps.status == status_filter){
  //         events_lst.push({title: ev.title, start:ev.start, status:ev.extendedProps.status, employee: ev.extendedProps.employee, customer: ev.extendedProps.customer})
  //       }
  //     }


  //     var filtered_calendar = new FullCalendar.Calendar(calendarEl, {
  //       initialView: 'dayGridMonth',
  //       editable: true,
  //       selectable: true,
  //       height: 550,
  //       select: function(selectionInfo){
  //         console.log(selectionInfo);
  //       },
  //       events : events_lst,
  //       eventDrop: function(event,dayDelta,minuteDelta,allDay,revertFunc) {
  //         alert(
  //           event.event.title + " was moved "
  //         );
  
  //         if (!confirm("Are you sure about this change?")) {
  //             revertFunc();
  //         }
  //     },
  //     eventClick: function(event, revertFunc){
  //       event_title = event.event.title
  //       new_title = prompt("Enter new title")
  //       if(new_title){
  //         event.event.setProp('title', new_title)     
  //       }
  //       if (!confirm("Are you sure you want to change the title?")) {
  //         revertFunc();
  //     }
  //     }
  //     });
  //     filtered_calendar.render();    
  //   })
    

  //   filterEmployeeBtn.addEventListener('click', () => {
  //     employee_filter = prompt("Which employee do you want to filter by?")
  //     all_events = calendar.getEvents()
  //     events_lst = []   

  //     for(ev of all_events){
  //       if(ev.extendedProps.employee == employee_filter){
  //         events_lst.push({title: ev.title, start:ev.start, status:ev.extendedProps.status, employee: ev.extendedProps.employee, customer: ev.extendedProps.customer})
  //       }
  //     }


  //     var filtered_calendar = new FullCalendar.Calendar(calendarEl, {
  //       initialView: 'dayGridMonth',
  //       editable: true,
  //       selectable: true,
  //       height: 550,
  //       select: function(selectionInfo){
  //         console.log(selectionInfo);
  //       },
  //       events : events_lst,
  //       eventDrop: function(event,dayDelta,minuteDelta,allDay,revertFunc) {
  //         alert(
  //           event.event.title + " was moved "
  //         );
  
  //         if (!confirm("Are you sure about this change?")) {
  //             revertFunc();
  //         }
  //     },
  //     eventClick: function(event, revertFunc){
  //       event_title = event.event.title
  //       new_title = prompt("Enter new title")
  //       if(new_title){
  //         event.event.setProp('title', new_title)     
  //       }
  //       if (!confirm("Are you sure you want to change the title?")) {
  //         revertFunc();
  //     }
  //     }
  //     });
  //     filtered_calendar.render();    
  //   })
    
  //   filterDateBtn.addEventListener('click', () => {
  //     date_filter = prompt("Which date do you want to filter by?")
  //     all_events = calendar.getEvents()
  //     events_lst = []   

  //     for(ev of all_events){
  //       if(ev.extendedProps.start == date_filter){
  //         events_lst.push({title: ev.title, start:ev.start, status:ev.extendedProps.status, employee: ev.extendedProps.employee, customer: ev.extendedProps.customer})
  //       }
  //     }


  //     var filtered_calendar = new FullCalendar.Calendar(calendarEl, {
  //       initialView: 'dayGridMonth',
  //       editable: true,
  //       selectable: true,
  //       height: 550,
  //       select: function(selectionInfo){
  //         console.log(selectionInfo);
  //       },
  //       events : events_lst,
  //       eventDrop: function(event,dayDelta,minuteDelta,allDay,revertFunc) {
  //         alert(
  //           event.event.title + " was moved "
  //         );
  
  //         if (!confirm("Are you sure about this change?")) {
  //             revertFunc();
  //         }
  //     },
  //     eventClick: function(event, revertFunc){
  //       event_title = event.event.title
  //       new_title = prompt("Enter new title")
  //       if(new_title){
  //         event.event.setProp('title', new_title)     
  //       }
  //       if (!confirm("Are you sure you want to change the title?")) {
  //         revertFunc();
  //     }
  //     }
  //     });
  //     filtered_calendar.render();    
  //   })

  // });

