<script>
export default {
  onLaunch: function () {
    console.log('App Launch')
  },
  onShow: function () {
    console.log('App Show')
  },
  onHide: function () {
    console.log('App Hide')
  }
}
</script>

<style>
/* 全局样式 */
page {
  background-color: #FAF7F2;
  color: #1B1B18;
  font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', sans-serif;
  font-size: 28rpx;
  line-height: 1.6;
}

.container {
  padding: 24rpx;
  padding-bottom: 100rpx; /* 避免被 tabBar 遮挡 */
}

.card {
  background: #FFFFFF;
  border-radius: 16rpx;
  padding: 32rpx;
  margin-bottom: 24rpx;
  box-shadow: 0 2rpx 12rpx rgba(0, 0, 0, 0.05);
}

.section-title {
  color: #B8860B;
  font-size: 32rpx;
  font-weight: 600;
  margin-bottom: 20rpx;
}

.text-muted {
  color: #6B6560;
  font-size: 24rpx;
}

.btn-primary {
  background-color: #B8860B;
  color: #FFFFFF;
  border-radius: 12rpx;
  padding: 20rpx 40rpx;
  font-size: 30rpx;
}
</style>
