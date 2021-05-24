const devices = document.querySelector('.devices');

document.addEventListener('DOMContentLoaded', function() {
  // nav menu
  const menus = document.querySelectorAll('.side-menu');
  M.Sidenav.init(menus, {edge: 'right'});
  // add device form
  const forms = document.querySelectorAll('.side-form');
  M.Sidenav.init(forms, {edge: 'left'});
});

// Render device data
const renderDevice = (data,id) => {
  if(data.price==0){
    data.price="Price not available";
  }else{
    data.price= `<i class="fa fa-rupee rupee-sign"></i>${data.price}`
  }
  const html = `<div class="card-panel device white row" data-id="${id}">
  <img src="${data.imgSrc}" alt="device thumb" class="device-image">
  <div class="device-details">
   <a target="_blank" href="${data.link}" class="device-link"> <div class="device-title">${data.title}</div></a>
    <div>
<span class="device-price">${data.price}</span>
    </div>
  </div>
  <div class="device-delete">
    <i class="material-icons delete-icon" data-id="${id}">delete_outline</i>
  </div>
</div>`;

devices.innerHTML += html;
};

// remove device from DOM
const removeDevice = (id) => {
  let device = document.querySelector(`.device[data-id=${id}]`);
  if(device==null){
      device=document.querySelector(`.delete-icon`);
  }
  device.remove();
};

const error=()=>{
  const html = `<div class="card-panel red lighten-2 pulse">This is a card panel with a teal lighten-2 class</div>`;
  devices.innerHTML= html;         


}