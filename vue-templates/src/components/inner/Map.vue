<template>
  <div>
    <div id="map" style="width:300px;height:300px;"></div>
  </div>
</template>

<script>
export default {
  name: "Map",
  data() {
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    } else {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      script.src = "//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=c39b70c857a7f27e0adc5039c85b7e66&libraries=services";

      document.head.appendChild(script);
    }
  },
  methods: {
    initMap() {
      const container = document.getElementById("map");
      const options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3,
      };

      this.map = new kakao.maps.Map(container, options);

      // 주소-좌표 변환 객체를 생성합니다
      this.geocoder = new kakao.maps.services.Geocoder();

      // 주소로 좌표를 검색합니다
      this.geocoder.addressSearch('경기 용인시 기흥구 흥덕1로 13 흥덕IT밸리', (result, status) => {
        // 정상적으로 검색이 완료됐으면 
        if (status === kakao.maps.services.Status.OK) {

          let bounds = new kakao.maps.LatLngBounds();
          
          bounds.extend(new kakao.maps.LatLng(result[0].y, result[0].x));
          let coords = new kakao.maps.LatLng(result[0].y, result[0].x);
          
          // 결과값으로 받은 위치를 마커로 표시합니다
          this.marker = new kakao.maps.Marker({
              map: this.map,
              position: coords
          });
          this.map.setBounds(bounds);

        } else {
          console.log('kakao maps services disconnected')
        }
      });


    },
  },
};
</script>

